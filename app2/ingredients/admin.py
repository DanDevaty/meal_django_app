from django.contrib import admin
from .models import Ingredient

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories', 'fat', 'glucose', 'measurement')
    list_filter = ('calories', 'fat', 'glucose', 'measurement')
    search_fields = ('name',)

