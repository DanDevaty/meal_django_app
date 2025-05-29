from django.urls import path
from .api_auth_views import CustomLoginAPIView

urlpatterns = [
    path('login/', CustomLoginAPIView.as_view(), name='api-login'),
]