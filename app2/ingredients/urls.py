from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ingredienceList, name='ingredients-list'),
    path('api/', include('ingredients.api_urls')),
]
