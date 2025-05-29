from django.urls import path, include
from .api_views import ShoppingListItem_view_set, ShoppingList_view_set
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'userlist', ShoppingList_view_set)
router.register(r'items', ShoppingListItem_view_set)

urlpatterns = [
    path('', include(router.urls)),
]
    