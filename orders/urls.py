from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('checkout-success/<int:order_id>/', views.checkout_success, name='checkout_success'),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('my-orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('mock-stk/<int:order_id>/', views.mock_stk_push, name='mock_stk_push'),
]
