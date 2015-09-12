from bongo.settings.common import *
import yaml

DEBUG = True

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

SECRET_KEY = 'afakesecretkeyfordevelopment'

SECURE_SSL_REDIRECT = False

# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': SITE_NAME,
        'USER': SITE_NAME,
        'PASSWORD': SITE_NAME,
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

ALLOWED_HOSTS = [
    '*'
]

INTERNAL_IPS = (
    '127.0.0.1',
    '0.0.0.0'
)

INSTALLED_APPS += (
)

TEST_RUNNER = 'bongo.settings.tests.ReusableRunner'

with open(os.path.normpath(os.path.join(SITE_ROOT, "ansible/env_vars/secure.yml")), "rb") as f:
    secrets = yaml.load(f)

    DISQUS_API_KEY = secrets['disqus_api_key']
    SCRIBD_API_KEY = secrets['scribd_api_key']
    SCRIBD_API_SECRET = secrets['scribd_api_secret']
    LOGENTRIES_TOKEN = secrets['logentries_token']
    MYSQL_PASS = secrets['mysql_pass']

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(SITE_ROOT, '.tmp/whoosh'),
        'STORAGE': 'file',
        'POST_LIMIT': 128 * 1024 * 1024,
        'BATCH_SIZE': 100,
    }
}
HAYSTACK_CONNECTIONS['test'] = HAYSTACK_CONNECTIONS['default']
