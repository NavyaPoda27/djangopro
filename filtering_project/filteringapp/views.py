
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
    name_filter = request.GET.get('name', '')
    min_age = request.GET.get('min_age', '')
    max_age = request.GET.get('max_age', '')
    email_filter = request.GET.get('email', '')

    persons = Person.objects.all()

    if name_filter:
        persons = persons.filter(name__icontains=name_filter)
    if min_age:
        persons = persons.filter(age__gte=min_age)
    if max_age:
        persons = persons.filter(age__lte=max_age)
    if email_filter:
        persons = persons.filter(email__icontains=email_filter)

    return render(request, 'person_list.html', {'persons': persons})

# Create your views here.
