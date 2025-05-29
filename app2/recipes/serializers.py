from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            'id', 'name', 'description', 'instructions', 'category',
            'preparation_time', 'servings', 'created_at', 'updated_at',
            'ingredients', 'created_by',
        ]
