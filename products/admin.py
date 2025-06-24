from django.contrib import admin
from .models import Product, Category, ProductImage
from django.utils.html import format_html
from .models import Product, Category, Brand, Attribute, AttributeValue, ProductVariant


# ✅ Inline admin for product images
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ('preview', 'image', 'alt_text', 'is_main')
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="80" height="80" style="object-fit: cover; border: 1px solid #ccc;" />',
                obj.image.url
            )
        return "-"
    preview.short_description = "Preview"


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1


# ✅ Product admin with image management
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]  # 👈 This enables gallery uploads
    exclude = ('slug',)
    list_display = ('name', 'price', 'stock', 'main_image_preview')
    search_fields = ('name',)
    list_filter = ('category',)

    def main_image_preview(self, obj):
        main_image = obj.images.filter(is_main=True).first()
        if main_image:
            return format_html('<img src="{}" width="80" height="80" style="object-fit: cover;" />', main_image.image.url)
        return "-"
    main_image_preview.short_description = "Main Image"


# ✅ Category admin (you can keep this simple)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('name', 'slug')
    search_fields = ('name',)


# ✅ Register everything
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

#admin.site.register(Brand)
admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(ProductVariant)
