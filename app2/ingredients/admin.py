from django.contrib import admin
from .models import Ingredient

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'calories',
        'protein',
        'saturated_fat',
        'carbohydrates',
        'sugar',
        'fiber',
        'salt',
        'measurement',
    )
    list_filter = (
        'measurement',
    )
    search_fields = ('name',)
