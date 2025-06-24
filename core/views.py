from django.shortcuts import render

from products.models import Product, Category

def homepage(request):
    featured = Product.objects.all()[:6]
    categories = Category.objects.all()[:4]
    return render(request, 'homepage.html', {
        'featured': featured,
        'categories': categories
    })
