from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# ✅ Shared function for filtering products
def filter_products(products, request):
    query = request.GET.get('q')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if query:
        products = products.filter(name__icontains=query)

    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    return products, query, min_price, max_price


# ✅ Show all products, with optional filters
def product_list(request):
    products = Product.objects.all()
    products, query, min_price, max_price = filter_products(products, request)

    all_categories = Category.objects.all()
    return render(request, 'products/product_list.html', {
        'products': products,
        'all_categories': all_categories,
        'query': query,
        'min_price': min_price,
        'max_price': max_price
    })


# ✅ Show products by category, with optional filters
def products_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    products, query, min_price, max_price = filter_products(products, request)

    all_categories = Category.objects.all()
    return render(request, 'products/product_list.html', {
        'products': products,
        'category': category,
        'all_categories': all_categories,
        'query': query,
        'min_price': min_price,
        'max_price': max_price
    })


# ✅ Show single product detail
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    variants = product.variants.prefetch_related('attribute_values')

    # Dynamically build a map of attribute name -> list of values
    attribute_map = {}
    for variant in variants:
        for attr_val in variant.attribute_values.all():
            attribute = attr_val.attribute.name
            attribute_map.setdefault(attribute, set()).add(attr_val.value)

    return render(request, 'products/product_detail.html', {
        'product': product,
        'attribute_map': attribute_map,
        'variants': variants
    })

