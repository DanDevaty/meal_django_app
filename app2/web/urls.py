
from django.contrib import admin
from django.urls import path, include  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipes/', include(('recipes.urls', 'recipes'), namespace='recipes')),
    path('ingredients/', include('ingredients.urls')),
    path('fridge/', include('fridge.urls')),
    path('', include('hello.urls')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('shoppinglist/', include('shoppingList.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/user/', include('users.api_urls')),
]

