from .base import *
from decouple import config
import os


DEBUG = True

USE_CLOUDINARY=False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite3')
}

print("Local media root:", MEDIA_ROOT)
