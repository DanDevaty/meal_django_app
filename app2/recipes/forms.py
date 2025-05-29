from django import forms
from .models import Recipe
from ingredients.models import Ingredient

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['created_by']
        widgets = {
            'ingredients': forms.SelectMultiple(attrs={'class': 'select2'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Zobrazí všechny ingredience
        self.fields['ingredients'].queryset = Ingredient.objects.all()
