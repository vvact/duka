from .base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite3')
}
