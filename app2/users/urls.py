app_name = 'users'
from django.urls import path, include
from .views import register_view, login_view, logout_view, profile_view
from users.views import google_login_redirect, edit_profile


urlpatterns = [
    path('accounts/google/login/callback/', google_login_redirect, name='google_login_redirect'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path("edit_profile/", edit_profile, name="edit_profile"),
    path('recipes/', include(('recipes.urls', 'recipes'))),
    path('api/', include('users.api_urls')),
    path('api/auth/', include('users.api_auth_urls')),
]