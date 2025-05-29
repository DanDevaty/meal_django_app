from django.db import models
from ingredients.models import Ingredient
from django.conf import settings


class ShoppingList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='shopping_lists')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.first_name}s shopping list ({self.created_at.date()})"


class ShoppingListItem(models.Model):
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE, related_name='items')
    ingredient = models.ForeignKey('ingredients.Ingredient', on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100, blank=True)
    is_purchased = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.ingredient.name} ({self.quantity})"