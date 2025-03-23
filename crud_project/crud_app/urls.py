from django.urls import path
from .views import index, insert, update, delete

urlpatterns = [
    path('', index, name='index'),  
    path('insert/', insert, name='insert'),  
    path('update/<int:id>/', update, name='update'), 
    path('delete/<int:id>/', delete, name='delete'),  
]
