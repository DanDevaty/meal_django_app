from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Fridge, Allergy, Food
from .forms import FoodForm

@login_required
def index(request):
    '''user = request.user

    # 🧊 Získání nebo vytvoření lednice pro uživatele
    fridge, created = Fridge.objects.get_or_create(user=user)

    # 🛡️ Ověření alergií
    allergies = Allergy.objects.filter(user=user)

    # ✅ Přidání jídla přes formulář
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            food = form.save()
            fridge.foods.add(food)
            return redirect('profile.html')  # nebo kamkoli přesměrovat
    else:
        form = FoodForm()

    # 📦 Seznam potravin
    foods = fridge.foods.all()

    # ⚠️ U každého jídla spočítej, jestli obsahuje alergen
    for food in foods:
        food.has_allergen = food.contains_allergen(allergies)
'''
    return render(request, 'fridge/index.html')

def ai_chat_page(request):
    return render(request, 'fridge/ai_chat.html')