"""
Django settings for bongo project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os
import sys
import yaml

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = os.path.dirname(BASE_DIR)

# Site name:
SITE_NAME = os.path.basename(BASE_DIR)

DEBUG = False

# Security settings

SECURE_BROWSER_XSS_FILTER = True
SECURE_FRAME_DENY = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Application definition

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangobower',
    'djangosecure',

    # Suit has to come before contrib.admin
    'suit',
    'django.contrib.admin',

    # Search
    'haystack',

    # Local apps
    'bongo.apps.bongo',
    'bongo.apps.archive',
    'bongo.apps.api',
    'bongo.apps.frontend',
    'bongo.apps.search',
    'bongo.apps.tasks',

    # for the frontend
    'compressor',

    # for the API
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
)

MIDDLEWARE_CLASSES = (
    'djangosecure.middleware.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'bongo.urls'

WSGI_APPLICATION = 'wsgi.application'


# Internationalization
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'America/New_York'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# https://docs.djangoproject.com/en/dev/topics/i18n/
USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'static'))
MEDIA_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'media'))

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
    'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS = (
    os.path.normpath(os.path.join(BASE_DIR, 'apps/frontend/assets')),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Brian Jacobel', 'bjacobel@gmail.com'),
    ('Andrew Daniels', 'adaniels@bowdoin.edu'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

LOGENTRIES_TOKEN = ''
try:
    with open(os.path.normpath(os.path.join(SITE_ROOT, "ansible/env_vars/secure.yml")), "rb") as f:
        secrets = yaml.load(f)
        LOGENTRIES_TOKEN = secrets['logentries_token']
except:
    LOGENTRIES_TOKEN = os.environ.get('LOGENTRIES_TOKEN')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
    'require_debug_false': {
        '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            '()': 'logutils.colorize.ColorizingStreamHandler',
            'stream': sys.stdout
        },
        'logentries': {
            'token': LOGENTRIES_TOKEN,
            'class': 'logentries.LogentriesHandler'
        }
    },
    'loggers': {
        'bongo': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'celery': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

SUIT_CONFIG = {
    'ADMIN_NAME': SITE_NAME
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            "context_processors": [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            "debug": DEBUG,
        },
        "DIRS": [
            os.path.normpath(os.path.join(BASE_DIR, 'templates')),
            os.path.normpath(os.path.join(BASE_DIR, 'apps/frontend/templates')),
            os.path.normpath(os.path.join(BASE_DIR, 'apps/search/templates')),
        ]
    }
]

### django-rest-framework ###

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_SERIALIZER_CLASS': 'bongo.apps.api.pagination.CustomPaginationSerializer',
    'PAGINATE_BY': 20,                  # Default to 20
    'PAGINATE_BY_PARAM': 'limit',       # Allow client to override, using `?limit=xxx`.
    'MAX_PAGINATE_BY': 100,             # Maximum limit allowed when using `?limit=xxx`.
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'COMPACT_JSON': False
}

API_VERSION = 1

### end drf ###

### django-cors-headers ###

CORS_ORIGIN_WHITELIST = (
    'bowdoinorient.co',
    'bowdoinorient.com',
)

### end django-cors-headers ###

### django-bower ###

BOWER_INSTALLED_APPS = (
    "moment#2.8.1",
    "zepto#1.1.4",
)

BOWER_PATH = os.path.join(SITE_ROOT, 'node_modules/bower/bin/bower')

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'static/bower_components')

### end django-bower ###

### django-compressor ###

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

COMPRESS_OFFLINE = True

### end django-compressor ###

### Haystack ###

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
        'INCLUDE_SPELLING': True
    },
    'test': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack_test',
        'INCLUDE_SPELLING': True
    },
}

### End Haystack ###