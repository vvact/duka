# models/attribute.py

from django.db import models
from .product import Product

class Attribute(models.Model):
    name = models.CharField(max_length=100)  # e.g. Size, RAM

    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)  # e.g. "42", "16GB"

    def __str__(self):
        return f"{self.attribute.name}: {self.value}"


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    sku = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    attribute_values = models.ManyToManyField(AttributeValue)

    def __str__(self):
        return f"{self.product.name} - {', '.join(str(v) for v in self.attribute_values.all())}"
