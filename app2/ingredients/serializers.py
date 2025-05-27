from rest_framework import serializers
from .models import Ingredient
from django.contrib.auth import get_user_model

User = get_user_model()

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']
        read_only_fields = ['email']
