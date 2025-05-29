from django.urls import path
from .views import index, ai_chat_page

urlpatterns = [
    path('', index, name='fridge_home'),  # ✅ přidáno jméno!
    path('chat/', ai_chat_page, name='ai_chat_page'),
]
