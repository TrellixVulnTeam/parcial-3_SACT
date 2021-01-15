"""
Django settings for Parcial3 project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
import cloudinary as cloudinary
import django_heroku
import mongoengine as mongoengine
import django_on_heroku

BASE_DIR = Path(__file__).resolve().parent.parent

BD_NAME = 'mongodb+srv://admin:ingenieriaWeb@cluster0.4qgt2.mongodb.net/parcial3?retryWrites=true&w=majority&ssl' \
          '=true&ssl_cert_reqs=CERT_NONE'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&izpjhr=x)g3qe+2_-lmn^@fukg7@k@x%01ks2ut=!)x-iefzh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_mongoengine',
    'client',
    'server',
    'gunicorn'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'Parcial3.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Parcial3.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


MONGODB_DATABASES = {
    'default': {
        'name': 'parcial3',
        "host": BD_NAME,
        "password": "ingenieriaWeb",
        "username": "admin",
    }
}


DATABASES = {
}

SESSION_ENGINE = 'django_mongoengine.sessions'
SESSION_SERIALIZER = 'django_mongoengine.sessions.BSONSerializer'
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

##SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

## google auth

GOOGLE_CLIENT_ID="701397416705-4npsqql9li0fcfud4d5dp43gj2kouii2.apps.googleusercontent.com"

##cloudinary

CLOUD_NAME = 'dvxk9pojd'
API_KEY = '977761672389298'
API_SECRET = '4T3IAHYyIKER0kwc6b0rgsUlAOI'

# Cloudinary config -> Si no va, probar sin variables de entorno.
cloudinary.config(
  cloud_name = CLOUD_NAME,
  api_key = API_KEY,
  api_secret = API_SECRET,
  secure = True
)

STATIC_ROOT = 'static'
STATICFILES_DIRS = (
    django_heroku.os.path.join(BASE_DIR, 'static'),
)


django_heroku.settings(locals())