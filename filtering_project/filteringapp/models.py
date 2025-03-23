from django.db import models
class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.CharField(max_length=15)


# Create your models here.
