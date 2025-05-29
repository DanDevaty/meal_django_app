# fridge/serializers.py
from rest_framework import serializers
from .models import FridgeItem

class FridgeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FridgeItem
        fields = '__all__'