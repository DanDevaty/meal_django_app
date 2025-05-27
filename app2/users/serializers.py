from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'  # explicitně email

    def validate(self, attrs):
        email = attrs.get(self.username_field)
        password = attrs.get("password")

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError({"detail": "Uživatel neexistuje."})

        if not user.check_password(password):
            raise serializers.ValidationError({"detail": "Nesprávné heslo."})

        if not user.is_active:
            raise serializers.ValidationError({"detail": "Uživatel není aktivní."})

        attrs['username'] = user.email  # JWT interní "username" pole musí být
        return super().validate(attrs)



class UserSerializer(serializers.ModelSerializer):
    allergies = serializers.StringRelatedField(many=True)

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'date_of_birth',
            'gender',
            'height_cm',
            'weight_kg',
            'daily_calorie_goal',
            'dietary_preferences',
            'allergies',
        ]
