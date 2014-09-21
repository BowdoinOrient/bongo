from common import *
from os.path import join, normpath
from os import environ

DEBUG = True

SECRET_KEY = open(
    normpath(
        join(BASE_DIR, 'settings/secrets/secret_key')
    )
).read().strip()

# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': SITE_NAME,
        'USER': SITE_NAME,
        'PASSWORD': SITE_NAME,
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

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

ALLOWED_HOSTS = [
    'localhost'
]

INSTALLED_APPS += (
    'django_nose',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = ['--with-fixture-bundling', '--nologcapture']

NOSE_TESTMATCH = '(?:^|[b_./-])[Tt]ests'

os.environ['REUSE_DB'] = '1'

REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}