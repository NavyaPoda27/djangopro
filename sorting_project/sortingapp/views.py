from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person
from faker import Faker
import random

def insert_rows(request):
    fake = Faker()
    for _ in range(50):
        Person.objects.create(
            name=fake.name(),
            age=random.randint(18, 80),
            email=fake.email()
        )
    return HttpResponse("50 records inserted successfully.")

def person_list(request):
    valid_fields = ['name', 'age', 'email']  # Only allow sorting by these fields
    sort_by = request.GET.get('sort', '').strip()  # Get sorting param, remove extra spaces
    order = request.GET.get('order', '').strip()  # Get order param (asc/desc)

    # Validate sorting field
    if sort_by not in valid_fields:
        sort_by = 'name'  # Default sorting field

    # Apply descending order if specified
    if order == "desc":
        sort_by = f"-{sort_by}"

    persons = Person.objects.all().order_by(sort_by)  # Safe sorting

    return render(request, 'person_list.html', {'persons': persons, 'sort_by': sort_by, 'order': order})




# Create your views here.
