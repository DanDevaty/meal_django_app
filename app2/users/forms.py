from django import forms
from django.contrib.auth import get_user_model
from alergies.models import Allergy
from .models import CustomUser
from fridge.models import FridgeItem
from django.contrib.auth import authenticate

ALLERGY_CHOICES = Allergy.ListOfAllergies
User = get_user_model()


class EmailLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        user = authenticate(email=email, password=password)
        if not user:
            raise forms.ValidationError("Neplatný email nebo heslo.")
        cleaned_data["user"] = user
        return cleaned_data

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Heslo", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Potvrdit heslo", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Hesla se neshodují.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'date_of_birth', 'gender',
            'height_cm', 'weight_kg', 'daily_calorie_goal', 'dietary_preferences'
        ]


class AllergyForm(forms.Form):
    name = forms.ChoiceField(
        choices=[('', '-- Vyber alergii --')] + Allergy.ListOfAllergies,
        required=False,
        label="Známá alergie",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    addDifAllergies = forms.CharField(
        required=False,
        label="Jiná alergie",
        widget=forms.TextInput(attrs={
            'placeholder': 'Napiš jinou alergii',
            'class': 'form-control'
        })
    )

class MealForm(forms.ModelForm):
    class Meta:
        model = FridgeItem
        fields = '__all__'

