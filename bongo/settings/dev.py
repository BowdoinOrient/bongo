from bongo.settings.common import *
import yaml

DEBUG = True

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
    '*'
]

INSTALLED_APPS += (
    'django_nose',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = ['--with-fixture-bundling', '--nologcapture']

NOSE_TESTMATCH = '(?:^|[b_./-])[Tt]ests'

os.environ['REUSE_DB'] = '1'

with open(os.path.normpath(os.path.join(SITE_ROOT, "ansible/env_vars/secure.yml")), "rb") as f:
    secrets = yaml.load(f)

    DISQUS_API_KEY = secrets['disqus_api_key']
    SCRIBD_API_KEY = secrets['scribd_api_key']
    SCRIBD_API_SECRET = secrets['scribd_api_secret']
    LOGENTRIES_TOKEN = secrets['logentries_token']

STATIC_URL ='/static/'
MEDIA_URL='/media/'

CELERY_ALWAYS_EAGER = True