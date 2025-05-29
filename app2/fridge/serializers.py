# fridge/serializers.py
from rest_framework import serializers
from .models import FridgeItem

class FridgeItemSerializer(serializers.ModelSerializer):
    food_name = serializers.CharField(source='food.name', read_only=True)

    class Meta:
        model = FridgeItem
        fields = ['id', 'food_name', 'expiration_date']
        
class FridgeImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField()