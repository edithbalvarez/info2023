#acá le digo que de base, importame todo, por eso el *
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        #engine = motor de base de datos
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR/ 'db.backends.sqlite3',
       
    }
}
