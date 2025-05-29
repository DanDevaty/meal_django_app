from rest_framework import viewsets
from .models import CustomUser
from .serializers import UserSerializer

class Users_view_set(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
