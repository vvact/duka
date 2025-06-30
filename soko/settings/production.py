from .base import *
from decouple import config
import dj_database_url

DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

# ✅ Cloudinary apps must be added
INSTALLED_APPS += [
    'cloudinary',
    'cloudinary_storage',
]

# ✅ Cloudinary storage settings
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': config('CLOUDINARY_API_KEY'),
    'API_SECRET': config('CLOUDINARY_API_SECRET'),
}

DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}

# Render uses HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
