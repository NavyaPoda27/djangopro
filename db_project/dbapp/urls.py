from django.urls import path
from .views import item_list, add_item

urlpatterns = [
    path('', item_list, name='item_list'),
    path('add/', add_item, name='add_item'),
]
