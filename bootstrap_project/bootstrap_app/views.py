from django.shortcuts import render
from .models import Product
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')
def product_list(request):
    if not Product.objects.exists():
        Product.objects.create(name='Swift Keyboard Pro',description='Ergonomic, Wireless, Backlit',price='59.99')
        Product.objects.create(name='AeroFlex Running Shoes',description='Lightweight, Durable, Breathable',price='89.99')
        Product.objects.create(name='Zenith Noise Canceller',description='Over-Ear, Active, Comfortable',price='129.99')
        Product.objects.create(name='GlideX Gaming Mouse',description='RGB, Precision, Wireless',price='49.99')
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


# Create your views here.
