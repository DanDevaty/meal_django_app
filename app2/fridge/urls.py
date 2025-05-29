from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index, name='fridge_home'),
    path('api/', include('fridge.api_urls'))
]
