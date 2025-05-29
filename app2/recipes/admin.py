from django.contrib import admin
from .models import Recipe
from .forms import RecipeForm

@admin.register(Recipe)
class ReceptAdmin(admin.ModelAdmin):
    form = RecipeForm
    list_display = ('name', 'category', 'servings', 'preparation_time', 'created_at')
    search_fields = ('name', 'description', 'category')
    list_filter = ('category', 'created_at')
    ordering = ('-created_at',)
    filter_horizontal = ('ingredients',) 
