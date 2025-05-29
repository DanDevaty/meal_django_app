from django.urls import path, include
from .api_views import Recipes_view_set
from rest_framework.routers import DefaultRouter
from recipes import api_views

router = DefaultRouter()
router.register(r'recipes', Recipes_view_set)

urlpatterns = [
    path('', include(router.urls)),
]
    