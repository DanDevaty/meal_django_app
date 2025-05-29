from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProfileForm, MealForm
from .models import CustomUser, Meal
from datetime import timedelta, date
from django.db.models import Sum
from .forms import EmailLoginForm

# MODELY Z OSTATNÍCH APLIKACÍ
from fridge.models import Fridge, Food, FridgeItem
from shoppingList.models import ShoppingList, ShoppingListItem
from alergies.models import Allergy
from recipes.models import Recipe
from ingredients.models import Ingredient

# FORMULÁŘE Z OSTATNÍCH APLIKACÍ
from fridge.forms import FoodForm
from shoppingList.forms import ShoppingListItemForm
from alergies.forms import UserProfileForm
from recipes.forms import RecipeForm
from users.forms import AllergyForm

# 🔐 REGISTRACE

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})

# 🔓 LOGIN

def login_view(request):
    if request.method == "POST":
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            login(request, form.cleaned_data["user"])
            return redirect("users:profile")  # nebo kamkoliv
    else:
        form = EmailLoginForm()
    return render(request, "users/login.html", {"form": form})

# 🚪 LOGOUT

def logout_view(request):
    logout(request)
    return redirect('login')

# 🌐 GOOGLE LOGIN CALLBACK

def google_login_redirect(request):
    user = request.user
    if not CustomUser.objects.filter(email=user.email).exists():
        logout(request)
        return redirect('register')  # přesměruj na registraci, pokud e-mail není v DB
    return redirect('profile')

# 👤 PROFIL/DASHBOARD

@login_required
def profile_view(request):
    user = request.user
    fridge, _ = Fridge.objects.get_or_create(user=user)
    profile = user

    food_form = FoodForm()
    shopping_form = ShoppingListItemForm()
    allergy_form = UserProfileForm(instance=profile)
    recipe_form = RecipeForm()
    meal_form = MealForm()
    all_foods = Food.objects.all()

    today = date.today()
    last_7_days = [today - timedelta(days=i) for i in range(6, -1, -1)]
    meals_per_day = {
        day: Meal.objects.filter(user=user, date=day).aggregate(total=Sum('calories'))['total'] or 0
        for day in last_7_days
    }

    calorie_chart_labels = [day.strftime('%a') for day in last_7_days]  # např. ['Po', 'Út', 'St']
    calorie_chart_data = list(meals_per_day.values()) 

    if request.method == 'POST':
        if 'add_food' in request.POST:
            food_form = FoodForm(request.POST)
            if food_form.is_valid():
                food = food_form.save()
                fridge.foods.add(food)
                return redirect('profile')

        elif 'add_food_direct' in request.POST:
            name = request.POST.get('name')
            expiration = request.POST.get('expiration_date')
            if name and expiration:
                food = Food.objects.create(name=name, expiration_date=expiration)
                fridge.foods.add(food)
            return redirect('profile')

        elif request.method == 'POST':
            if 'add_existing_food' in request.POST:
                food_id = request.POST.get('existing_food_id')
                expiration_date = request.POST.get('existing_expiration_date')

                if food_id and expiration_date:
                    food = get_object_or_404(Food, id=food_id)
                    
                    # Vytvoření FridgeItem - přidání potraviny do lednice uživatele
                    FridgeItem.objects.create(
                        fridge=fridge,
                        food=food,
                        expiration_date=expiration_date
                    )
                    return redirect('profile')

        elif 'delete_food' in request.POST:
            food_id = request.POST.get('delete_food')
            try:
                food = Food.objects.get(id=food_id)
                fridge.foods.remove(food)
            except Food.DoesNotExist:
                pass
            return redirect('profile')

        elif 'add_item' in request.POST:
            shopping_form = ShoppingListItemForm(request.POST)
            if shopping_form.is_valid():
                item = shopping_form.save(commit=False)
                item.user = user
                item.save()
                return redirect('profile')

        elif 'save_allergy' in request.POST:
            allergy_form = AllergyForm(request.POST)
            if allergy_form.is_valid():
                selected_name = allergy_form.cleaned_data.get('name')
                other_name = allergy_form.cleaned_data.get('addDifAllergies').strip()

                allergy_obj = None

                if selected_name:
                    allergy, created = Allergy.objects.get_or_create(name=selected_name.strip())
                    allergy.profiles.add(user)

                if other_name:
                    allergy, created = Allergy.objects.get_or_create(name=other_name.strip())
                    allergy.profiles.add(user)

                if allergy_obj:
                    user.allergies.add(allergy_obj)

            return redirect('profile')

        elif 'delete_allergy' in request.POST:
            allergy_id = request.POST.get('delete_allergy')
            try:
                allergy = Allergy.objects.get(id=allergy_id)
                profile.allergies.remove(allergy)
            except Allergy.DoesNotExist:
                pass
            return redirect('profile')

        elif 'add_recipe' in request.POST:
            recipe_form = RecipeForm(request.POST)
            if recipe_form.is_valid():
                recipe = recipe_form.save(commit=False)
                recipe.created_by = user
                recipe.made_with = Ingredient.objects.first()
                recipe.save()
                return redirect('profile')
        
        elif 'add_meal' in request.POST:
            food_name = request.POST.get('food_name', '').strip()
            calories = request.POST.get('calories', '').strip()

            if food_name and calories.isdigit():
                calories = int(calories)
                # Vytvoření záznamu Meal
                Meal.objects.create(user=user, name=food_name, calories=calories, date=date.today())
                return redirect('profile')
    
    fridge_items = fridge.items.select_related('food').all()

    return render(request, 'users/profile.html', {
        'user': user,
        'food_form': food_form,
        'shopping_form': shopping_form,
        'allergy_form': allergy_form,
        'recipe_form': recipe_form,
        'all_foods': all_foods,
        'list_of_allergies': Allergy.ListOfAllergies if hasattr(Allergy, 'ListOfAllergies') else [],
        'addDifAllergies': Allergy.addDifAllergies if hasattr(Allergy, 'addDifAllergies') else None,
        'calorie_chart_labels': calorie_chart_labels,
        'calorie_chart_data': calorie_chart_data,
        'fridge_items': fridge_items,
    })

# ✏️ ÚPRAVA PROFILU

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=user)
    return render(request, 'users/edit_profile.html', {'form': form})