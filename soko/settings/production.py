from .base import *

DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}

# Render uses HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
