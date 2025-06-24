from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    PAYMENT_METHOD_CHOICES = [
        ('cod', 'Pay on Delivery'),
        ('mpesa', 'Pay with M-Pesa'),
    ]

    MPESA_METHOD_CHOICES = [
        ('stk', 'M-Pesa STK Push'),
        ('till', 'M-Pesa Till Number'),
    ]

    payment_method = forms.ChoiceField(
        choices=PAYMENT_METHOD_CHOICES,
        widget=forms.RadioSelect,
    )

    mpesa_option = forms.ChoiceField(
        choices=MPESA_METHOD_CHOICES,
        widget=forms.RadioSelect,
        required=False  # only shown when M-Pesa is selected
    )

    class Meta:
        model = Order
        fields = ['name', 'phone', 'address', 'payment_method']
