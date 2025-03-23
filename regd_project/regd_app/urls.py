from django.urls import path
from .views import register_view
from .views import home_view
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('register/', register_view, name='register'),
    path("home/", home_view, name="home"), 
    path("logout/", LogoutView.as_view(), name="logout"),
]