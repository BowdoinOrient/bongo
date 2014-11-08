from os import environ
from bongo.settings.common import *

# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': SITE_NAME,
        'USER': SITE_NAME,
        'PASSWORD': environ.get("{}_POSTGRES_PASS".format(SITE_NAME.upper())),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
    'archive': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DB02Orient',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = environ.get('{}_SECRET_KEY'.format(SITE_NAME.upper()), '')

# See: http://django-storages.readthedocs.org/en/latest/index.html
INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    '.bjacobel.com',
    '.bowdoinorient.com'
]

########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
########## END CACHE CONFIGURATION


########## AMAZON CONFIGURATION

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_STORAGE_BUCKET_NAME = "bowdoinorient-bongo"
AWS_ACCESS_KEY_ID = environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = environ.get("AWS_SECRET_ACCESS_KEY")
S3_URL = 'http://s3.amazonaws.com/{}'.format(AWS_STORAGE_BUCKET_NAME)

STATIC_URL = S3_URL + "/static/"
MEDIA_URL = S3_URL + "/media/"

########## END AMAZON

#### RAVEN ###

RAVEN_CONFIG = {
    'dsn': environ.get('{}_RAVEN_DSN'.format(SITE_NAME.upper())),
}

### END RAVEN #####