from django.urls import path
from .views import add_to_cart, view_cart, clear_cart

urlpatterns = [
    path('addcart/', add_to_cart, name='add_to_cart'),
    path('viewcart/', view_cart, name='view_cart'),
    path('clearcart/', clear_cart, name='clear_cart'),
]
