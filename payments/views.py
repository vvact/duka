from django.shortcuts import render, get_object_or_404
from orders.models import Order
from .utils import send_stk_push_request

def mpesa_stk_push(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    
    success = send_stk_push_request(order)  # ✅ Make sure this line exists

    if success:
        return render(request, "payments/processing.html", {"order": order})
    else:
        return render(request, "payments/payment_error.html", {"order": order})
