"""
Django settings for django_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(   _DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Marker for local deployment
IS_LOCAL = os.path.isfile(os.path.join(os.path.dirname(__file__), "..", ".local"))

PROJECT_DIR = os.path.join(os.path.dirname(__file__), "..")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sVRomwETUhjAESoAjQeIti9XvXDj0bYCL0Q41e8gu2QLlOmqmo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'clients',
    'home',
    'coupons',
    'paypal.standard.ipn',
    'djacobs_apns',
    'pushmonkey',
    'south',
    'stats',
    'backup',
    'plans',
    'emails',
    'contact_messages',
    'affiliates',
    'django_jfu_pushmonkey',
    'imagekit',
    'django_push_package',
    'website_clusters'    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_project.urls'

WSGI_APPLICATION = 'django_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
if IS_LOCAL:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': os.path.join(PROJECT_DIR, 'sqlite3.db'),  # Or path to database file if using sqlite3.
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'django',
            'USER': 'django',
            'PASSWORD': 'k1ods9C8lw',
            'HOST': 'localhost',
            'PORT': '',
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

if IS_LOCAL:
    STATICFILES_DIRS = ( os.path.join(os.path.dirname(__file__), 'static'),)

# PayPal
PAYPAL_TEST = False
if PAYPAL_TEST:
    PAYPAL_RECEIVER_EMAIL = "payments-facilitator@getpushmonkey.com" #sandbox
else:
    PAYPAL_RECEIVER_EMAIL = "payments@getpushmonkey.com" #production
PAYPAL_SUBSCRIPTION_IMAGE = "/static/images/paypal-button.png"
PAYPAL_SUBSCRIPTION_SANDBOX_IMAGE = "/static/images/paypal-button.png"

# Email Config
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.socketlabs.com'
EMAIL_HOST_USER = 'server14980'
EMAIL_HOST_PASSWORD = 'Ax9o2E4Fsb6K7Qi'
EMAIL_PORT = 25
DEFAULT_FROM_EMAIL = 'Push Monkey <mailer@getpushmonkey.com>'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

# MEDIA
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media/')
MEDIA_URL = '/static/media/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'
