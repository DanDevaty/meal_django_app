from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .api_views import Ingredients_view_set


router = DefaultRouter()
router.register(r'items', Ingredients_view_set)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]