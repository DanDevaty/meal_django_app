from django.shortcuts import render
from .models import Ingredient


def ingredienceList(request):
    ingredience = Ingredient.objects.all()
    return render(request, 'index.html', {'ingredience': ingredience})
