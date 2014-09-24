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
    'djsupervisor',
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
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
########## END CACHE CONFIGURATION


#### RAVEN ###

RAVEN_CONFIG = {
    'dsn': environ.get('{}_RAVEN_DSN'.format(SITE_NAME.upper())),
}

### END RAVEN #####

###### LOGENTRIES #####

from logentries import LogentriesHandler
import logging

'handlers': {
    'logentries_handler': {
        'token': environ.get('{}_LOGENTRIES_TOKEN'.format(SITE_NAME.upper())),
        'class': 'logentries.LogentriesHandler'
    },
}

'loggers': {
    'logentries': {
        'handlers': ['logentries_handler'],
        'level': 'INFO',
    },
}