from .base import *

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['*']

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbname',
        'USER' : 'dbusername',
        'PASSWORD' : 'dbpass',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}
"""


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
STATIC_ROOT = 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')