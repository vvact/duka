from django.db import models
from products.models import Product

class Order(models.Model):

    PAYMENT_METHODS = [
        ('cod', 'Pay on Delivery'),
        ('mpesa', 'M-Pesa'),
    ]

    payment_method = models.CharField(
        max_length=10,
        choices=PAYMENT_METHODS,
        default='cod'
    )
    is_paid = models.BooleanField(default=False)

    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    #order status
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending',
    )

    def __str__(self):
        return f"Order #{self.id} by {self.name}"

    def get_total(self):
        return sum(item.total_price() for item in self.items.all())
    
    def get_total_cost(self):
        return sum(item.price * item.quantity for item in self.items.all())

    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def total_price(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
