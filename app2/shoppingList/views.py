from django.shortcuts import render, redirect
from .models import ShoppingList, Ingredient
from .forms import ShoppingListItemForm

def shopping_list(request):
    shopping_lists = ShoppingList.objects.filter(user=request.user)
    return render(request, 'ingredients/shopping_list.html', {'shopping_lists': shopping_lists})

def add_to_shopping_list(request):
    if request.method == 'POST':
        form = ShoppingListItemForm(request.POST)
        if form.is_valid():
            shopping_list_item = form.save(commit=False)
            shopping_list_item.user = request.user
            shopping_list_item.save()
            return redirect('shopping_list')
    else:
        form = ShoppingListItemForm()
    return render(request, 'ingredients/add_to_shopping_list.html', {'form': form})
