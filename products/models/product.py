from django.db import models
from django.utils.text import slugify
from .utils import generate_unique_slug

from django.db import models
from .category import Category
#from .brand import Brand

from django.urls import reverse


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, editable=False)  # 👈 not editable in admin
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)


    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

    @property
    def main_image(self):
        return self.images.filter(is_main=True).first() or self.images.first()
