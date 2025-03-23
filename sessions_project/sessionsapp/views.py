from django.shortcuts import render, redirect
def add_to_cart(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_cost = float(request.POST.get('item_cost', 0))
        
        cart = request.session.get('cart', [])
        cart.append({'name': item_name, 'cost': item_cost})
        request.session['cart'] = cart
    
    return redirect('view_cart')
def view_cart(request):
    cart = request.session.get('cart', [])
    total_cost = sum(item['cost'] for item in cart)
    return render(request, 'cart.html', {'cart': cart, 'total_cost': total_cost})

def clear_cart(request):
    request.session['cart'] = []
    return redirect('view_cart')



# Create your views here.
