from django.db import models
from django.conf import settings
from ingredients.models import Ingredient

class Food(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField(help_text="Comma-separated list of ingredients", blank=True)

    def __str__(self):
        return self.name

    def contains_allergen(self, allergies):
        ingredient_list = [i.strip().lower() for i in self.ingredients.split(',')]
        allergy_list = [a.name.lower() for a in allergies]
        return any(allergen in ingredient_list for allergen in allergy_list)

class Fridge(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient, blank=True)

    def __str__(self):
        return f"Fridge of {self.user.email}"

class FridgeItem(models.Model):
    fridge = models.ForeignKey(Fridge, on_delete=models.CASCADE, related_name='items')
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    expiration_date = models.DateField()

    def __str__(self):
        return f"{self.food.name} (exp: {self.expiration_date})"

class Allergy(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} (for {self.user.email})"
