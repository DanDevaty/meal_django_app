
from django.contrib import admin
from django.urls import path, include  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipes/', include('recipes.urls')), 
    path('ingredients/', include('ingredients.urls')),
    path('fridge/', include('fridge.urls')),  # <-- přidáš tuto řádku
    path('', include('hello.urls')),
    path('users/', include('users.urls')), 
    path('shoppingList/', include('shoppingList.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/user/', include('users.api_urls')),
    path('api/fridge/', include('fridge.api_urls')),

]

