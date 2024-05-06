from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # URL for login page
    path('register/', views.registration_view, name='register'),  # URL for registration page
    # Add more authentication-related URLs as needed
]
