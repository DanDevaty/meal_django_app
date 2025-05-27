from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers, viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model

from .serializers import UserSerializer, ItemSerializer
from .models import Ingredient

User = get_user_model()

# --- JWT Custom Token Serializer a View ---

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email' 

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({"detail": "Uživatel neexistuje."})

        if not user.check_password(password):
            raise serializers.ValidationError({"detail": "Nesprávné heslo."})

        if not user.is_active:
            raise serializers.ValidationError({"detail": "Uživatel není aktivní."})

        attrs['email'] = user.email  # důležité pro JWT interně
        return super().validate(attrs)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# --- User detail API ---

class UserDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

# --- Ingredient API ViewSet s JWT autentizací ---

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
