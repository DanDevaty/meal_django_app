from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .api_views import FridgeItem_view_set


router = DefaultRouter()
router.register(r'items', FridgeItem_view_set)

urlpatterns = [
    path('', include(router.urls)),
]