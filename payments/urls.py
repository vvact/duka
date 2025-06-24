from django.urls import path
from .views import mpesa_stk_push

urlpatterns = [
    path('stk-push/<int:order_id>/', mpesa_stk_push, name='mpesa_stk_push'),
]
