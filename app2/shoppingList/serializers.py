from rest_framework import serializers
from .models import ShoppingList, ShoppingListItem

class ShoppingList_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields =  '__all__'
        
class ShoppingListItem_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingListItem
        fields = '__all__'