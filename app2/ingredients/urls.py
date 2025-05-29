from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ingredientsList, name='ingredients-list'),
    path('api/', include('ingredients.api_urls')),
]
