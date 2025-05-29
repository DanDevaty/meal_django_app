from django import forms
from .models import FridgeItem


class FoodForm(forms.ModelForm):
    class Meta:
        model = FridgeItem
        fields = ['name', 'quantity', 'expiration_date']
        widgets = {
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user:
            instance.user = user
        if commit:
            instance.save()
        return instance
