app_name = 'recipes'

from django.urls import path, include
from . import views
from .api_views import Recipes_view_set
from recipes import views as recipes_views

urlpatterns = [
    path('', views.recipes_list, name='recipes_list'),
    path('api/', include('recipes.api_urls')),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/add/', views.recipe_create, name='recipe_create'),
    path('recipe/<int:pk>/edit/', views.recipe_update, name='recipe_update'),
]
