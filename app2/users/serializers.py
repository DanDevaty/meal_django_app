from rest_framework import serializers
from .models import CustomUser


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
