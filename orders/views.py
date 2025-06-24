from django.shortcuts import render, redirect
from .models import Order, OrderItem
from cart.cart import Cart
from django.shortcuts import get_object_or_404
import time
from .forms import OrderForm

from django.contrib.auth.decorators import login_required

from .models import Order
def checkout(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()

            # Create OrderItems from cart
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['product'].price,
                    quantity=item['quantity']
                )

            # Payment method handling
            payment_method = form.cleaned_data['payment_method']

            if payment_method == 'mpesa':
                mpesa_option = request.POST.get('mpesa_option')
                if mpesa_option == 'stk':
                    return redirect('payments:mpesa_stk_push', order_id=order.id)
                elif mpesa_option == 'till':
                    order.is_paid = True
                    order.status = 'confirmed'
                    order.save()
                    cart.clear()
                    return redirect('orders:checkout_success', order_id=order.id)

            elif payment_method == 'cod':
                order.status = 'pending'
                order.save()
                cart.clear()
                return redirect('orders:checkout_success', order_id=order.id)

    else:
        form = OrderForm()

    return render(request, 'orders/checkout.html', {
        'form': form,
        'cart': cart
    })



#@login_required
def my_orders(request):
    order_ids = request.session.get('orders', [])
    orders = Order.objects.filter(id__in=order_ids).order_by('-created_at')
    return render(request, 'orders/my_orders.html', {'orders': orders})


#@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order_detail.html', {'order': order})



def mock_stk_push(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    # Simulate STK push by marking as paid
    order.is_paid = True
    order.save()

    return redirect('checkout_success', order_id=order.id)


def checkout_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/checkout_success.html', {'order': order})
