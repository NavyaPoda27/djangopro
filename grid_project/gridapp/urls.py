from django.urls import path 
from .views import grid_view 
urlpatterns = [ 
    path("", grid_view, name='grid_view') 
] 