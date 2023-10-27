from django.urls import path

from .views import *

urlpatterns = [
    path('login', LoginView, name='user_login'),
    path('register', register, name='user_register'),
    path('logout', logout_view, name='user_logout'),
    path('profile', profile_view, name='user_profile'),
]
