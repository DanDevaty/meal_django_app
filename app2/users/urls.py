from django.urls import path
from .views import register_view, login_view, logout_view, profile_view
from users import views
from users.views import google_login_redirect


urlpatterns = [
    path('accounts/google/login/callback/', google_login_redirect, name='google_login_redirect'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path('<int:pk>/', views.recipe_detail, name='recipe_detail'),
    
    

]
