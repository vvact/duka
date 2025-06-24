from django.shortcuts import redirect, render, get_object_or_404
from .cart import Cart
from products.models import Product
from django.views.decorators.http import require_POST

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.add(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {
        'cart': cart,
        'cart_items': list(cart),  # optional, since __iter__ is defined
    })

def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)
    return redirect('cart:cart_detail')  # ✅ FIXED

@require_POST
def cart_update(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    try:
        quantity = int(request.POST.get('quantity', 1))
    except ValueError:
        quantity = 1
    cart.update(product, quantity)
    return redirect('cart:cart_detail')
