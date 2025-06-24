from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('product', 'quantity', 'price', 'total_price')
    can_delete = False
    extra = 0

    def total_price(self, obj):
        return obj.total_price()

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'payment_method', 'is_paid', 'created_at')
    list_filter = ('status', 'payment_method', 'is_paid', 'created_at')
    search_fields = ('name', 'phone', 'address')
    inlines = [OrderItemInline]


    def total_amount(self, obj):
        return obj.get_total()
