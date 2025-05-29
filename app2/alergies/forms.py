from django import forms
from .models import Allergy
from users.models import CustomUser

class UserProfileForm(forms.ModelForm):
    allergies = forms.ModelMultipleChoiceField(
        queryset=Allergy.objects.all().order_by('name'),
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-check-input'
        }),
        required=False,
        label="❗ Vyber své alergie:"
    )

    class Meta:
        model = CustomUser
        fields = ['allergies']
