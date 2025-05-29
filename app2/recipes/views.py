from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms import RecipeForm

def recipes_list(request):
    recipes = Recipe.objects.all()
    for recipe in recipes:
        if hasattr(recipe, 'preparation_time') and recipe.preparation_time:
            total_seconds = recipe.preparation_time.total_seconds()
            hours = int(total_seconds // 3600)
            minutes = int((total_seconds % 3600) // 60)

            if hours > 0:
                recipe.formatted_preparation_time = f"{hours}h {minutes}m"
            else:
                recipe.formatted_preparation_time = f"{minutes}m"
        else:
            recipe.formatted_preparation_time = "N/A"
    return render(request, 'recipes_list.html', {'recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.created_by = request.user
            recipe.save()
            form.save_m2m()  # ulož M2M vztahy (ingredients)
            return redirect('recipes:recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'recipe_form.html', {'form': form})

def recipe_update(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipe_form.html', {'form': form})
