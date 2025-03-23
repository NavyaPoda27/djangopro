from django.urls import path
from .views import person_list,insert_rows

urlpatterns = [
    path('', person_list, name='person_list'),        
    path('insert/', insert_rows, name='insert'), 
]
