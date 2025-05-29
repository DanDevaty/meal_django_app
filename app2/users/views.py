from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import timedelta, date
from django.db.models import Sum
from .forms import CustomUserCreationForm, EmailLoginForm, MealForm, ProfileForm
from .models import CustomUser, Meal
from fridge.models import FridgeItem, WatchedItem
from shoppingList.models import ShoppingListItem
from alergies.models import Allergy
from recipes.models import Recipe
from recipes.forms import RecipeForm
from ingredients.models import Ingredient
from django.contrib.auth import login, logout, authenticate
from fridge.forms import FoodForm
from shoppingList.forms import ShoppingListItemForm
from users.forms import AllergyForm

@login_required
def profile_view(request):
    user = request.user

    # Formuláře
    food_form = FoodForm()
    shopping_form = ShoppingListItemForm()
    allergy_form = AllergyForm()
    recipe_form = RecipeForm()
    meal_form = MealForm()

    # Data pro graf
    today = date.today()
    last_7_days = [today - timedelta(days=i) for i in range(6, -1, -1)]
    meals_per_day = {
        day: Meal.objects.filter(user=user, date=day).aggregate(total=Sum('calories'))['total'] or 0
        for day in last_7_days
    }
    calorie_chart_labels = [day.strftime('%a') for day in last_7_days]
    calorie_chart_data = list(meals_per_day.values())

    # POST logika
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'add_food':
            food_form = FoodForm(request.POST)
            if food_form.is_valid():
                food_form.save(user=request.user)  # můžeš přizpůsobit podle nového Food modelu
                return redirect('users:profile')

        elif action == 'add_meal':
            food_name = request.POST.get('food_name', '').strip()
            calories = request.POST.get('calories', '').strip()
            if food_name and calories.isdigit():
                Meal.objects.create(user=user, name=food_name, calories=int(calories), date=today)
                return redirect('users:profile')

        elif action == 'add_item':
            shopping_form = ShoppingListItemForm(request.POST)
            if shopping_form.is_valid():
                item = shopping_form.save(commit=False)
                item.user = user
                item.save()
                return redirect('users:profile')

        elif action == 'save_allergy':
            allergy_form = AllergyForm(request.POST)
            if allergy_form.is_valid():
                allergy_name = allergy_form.cleaned_data.get('name')
                other = allergy_form.cleaned_data.get('addDifAllergies')
                for name in [allergy_name, other]:
                    if name:
                        allergy, _ = Allergy.objects.get_or_create(name=name.strip())
                        allergy.profiles.add(user)
                return redirect('users:profile')

        elif action == 'delete_allergy':
            allergy_id = request.POST.get('delete_allergy')
            try:
                allergy = Allergy.objects.get(id=allergy_id)
                user.allergies.remove(allergy)
            except Allergy.DoesNotExist:
                pass
            return redirect('users:profile')

        elif action == 'add_recipe':
            recipe_form = RecipeForm(request.POST)
            if recipe_form.is_valid():
                recipe = recipe_form.save(commit=False)
                recipe.created_by = user
                recipe.made_with = Ingredient.objects.first()  # toto je potřeba upravit
                recipe.save()
                return redirect('users:profile')

    fridge_items = FridgeItem.objects.filter(user=user).all()
    watched_items = WatchedItem.objects.filter(user=user)

    return render(request, 'users/profile.html', {
        'user': user,
        'food_form': food_form,
        'shopping_form': shopping_form,
        'allergy_form': allergy_form,
        'recipe_form': recipe_form,
        'meal_form': meal_form,
        'calorie_chart_labels': calorie_chart_labels,
        'calorie_chart_data': calorie_chart_data,
        'fridge_items': fridge_items,
        'watched_items': watched_items,
    })


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            login(request, form.cleaned_data["user"])
            return redirect("users:profile")
    else:
        form = EmailLoginForm()
    return render(request, "users/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('users:login')


def google_login_redirect(request):
    user = request.user
    if not CustomUser.objects.filter(email=user.email).exists():
        logout(request)
        return redirect('users:register')
    return redirect('users:profile')

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = ProfileForm(instance=user)
    return render(request, 'users/edit_profile.html', {'form': form})