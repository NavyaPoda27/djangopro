from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
def add_to_cart(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_cost = float(request.POST.get('item_cost', 0))
        
        cart = json.loads(request.COOKIES.get('cart', '[]'))
        cart.append({'name': item_name, 'cost': item_cost})
        response = redirect('view_cart')
        response.set_cookie('cart', json.dumps(cart))
        return response
def view_cart(request):
    cart = json.loads(request.COOKIES.get('cart', '[]'))
    total_cost = sum(item['cost'] for item in cart)
    return render(request, 'cart.html', {'cart': cart, 'total_cost': total_cost})

def clear_cart(request):
    response = redirect('view_cart')
    response.delete_cookie('cart')
    return response





# Create your views here.
