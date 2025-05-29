from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .api_views import Users_view_set
from rest_framework import serializers


router = DefaultRouter()
router.register(r'users', Users_view_set)

urlpatterns = [
    path('', include(router.urls)),
]
