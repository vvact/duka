from .base import *

DEBUG = config('DEBUG', default=False, cast=bool)


# Allowed Hosts
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Database
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}