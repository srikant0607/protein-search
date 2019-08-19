import os
from .base import *
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ENVIRONMENT = 'local'
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Zoso',
        'USER': 'Zoso',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

