from django.urls import path
from .api_views import CustomTokenObtainPairView, UserDetailAPIView

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('me/', UserDetailAPIView.as_view(), name='user_detail'),
]
