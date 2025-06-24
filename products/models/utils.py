from django.utils.text import slugify

def generate_unique_slug(model_class, field_value):
    base_slug = slugify(field_value)
    slug = base_slug
    num = 1

    while model_class.objects.filter(slug=slug).exists():
        slug = f"{base_slug}-{num}"
        num += 1

    return slug
