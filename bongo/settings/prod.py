from os import environ
from common import *

# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': SITE_NAME,
        'USER': SITE_NAME,
        'PASSWORD': environ.get("{}_POSTGRES_PASS".format(SITE_NAME.upper())),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = environ.get('{}_SECRET_KEY'.format(SITE_NAME.upper()), '')

# See: http://django-storages.readthedocs.org/en/latest/index.html
INSTALLED_APPS += (
    'djsupervisor',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    '.bjacobel.com',
    '.bowdoinorient.com'
]