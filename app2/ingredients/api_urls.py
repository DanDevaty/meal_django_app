from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import ItemViewSet, CustomTokenObtainPairView, UserDetailAPIView

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('user/', UserDetailAPIView.as_view(), name='user_detail'), 
    path('', include(router.urls)),
]
