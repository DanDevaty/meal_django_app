from django.urls import path, include
from . import views

urlpatterns = [
    path('api/', include('shoppingList.api_urls')),
    path('shopping-list/', views.shopping_list, name='shopping_list'),
    path('add-to-shopping-list/', views.add_to_shopping_list, name='add_to_shopping_list'),
]