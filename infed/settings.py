import os

import django

DEBUG = os.environ.get('DJANGO_DEBUG') in ('yes', 'on')

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '*').split()

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'idm_brand',
    'infed',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.' + (
            'postgresql' if django.VERSION >= (1, 9) else 'postgresql_psycopg2'),
        'NAME': os.environ.get('DATABASE_NAME', 'infed'),
    },
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': (
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.static',
            ),
        },
    },
]

STATIC_URL = '/static/'

ROOT_URLCONF = 'infed.urls'

