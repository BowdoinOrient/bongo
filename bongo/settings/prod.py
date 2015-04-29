from os import environ
from bongo.settings.common import *

SECURE_SSL_REDIRECT = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': environ.get("DATABASE_NAME", ""),
        'USER': environ.get("DATABASE_USER", ""),
        'PASSWORD': environ.get("DATABASE_PASSWORD", ""),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
    'archive': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': environ.get("LEGACY_DB_NAME", ""),
        'USER': environ.get("LEGACY_DB_USER", ""),
        'PASSWORD': environ.get("LEGACY_DB_PASSWORD", ""),
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

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

AWS_ACCESS_KEY_ID = environ.get("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = environ.get("AWS_SECRET_ACCESS_KEY", "")
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_EXPIRE = 63115200
S3_URL = 'http://static.bowdoinorient.co/' # @TODO make this https and .com

STATIC_URL = S3_URL
MEDIA_URL = S3_URL

########## END AMAZON

#### RAVEN ###

RAVEN_CONFIG = {
    'dsn': environ.get('RAVEN_DSN'),
}

### END RAVEN #####

### DJANGO-COMPRESSOR SETTINGS ###

COMPRESS_CSS_FILTERS = (
    "compressor.filters.cssmin.CSSMinFilter",
)

COMPRESS_JS_FILTERS = (
    "compressor.filters.jsmin.JSMinFilter",  # this is actually the default but :shrug:
)

COMPRESS_STORAGE = STATICFILES_STORAGE

### END DJANGO-COMPRESSOR ###

DISQUS_API_KEY = environ.get('DISQUS_API_KEY', '')
SCRIBD_API_KEY = environ.get('SCRIBD_API_KEY', '')
SCRIBD_API_SECRET = environ.get('SCRIBD_API_SECRET', '')

for logger in LOGGING['loggers']:
    LOGGING['loggers'][logger]['handlers'].append('logentries')