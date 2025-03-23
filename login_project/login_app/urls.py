from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import home_view
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', home_view, name='home'),
    path('accounts/', include('django.contrib.auth.urls')), 
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
]
