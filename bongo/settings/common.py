"""
Django settings for bongo project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = os.path.dirname(BASE_DIR)

# Site name:
SITE_NAME = os.path.basename(BASE_DIR)

DEBUG = False

TEMPLATE_DEBUG = DEBUG

# Application definition

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangobower',

    # Suit has to come before contrib.admin
    'suit',
    'django.contrib.admin',

    # Local apps
    'bongo.apps.bongo',
    'bongo.apps.archive',
    'bongo.apps.api',
    'bongo.apps.frontend',
    'bongo.apps.celery',

    # for the frontend
    'compressor',

    # for the API
    'rest_framework',
    'corsheaders',
)

MIDDLEWARE_CLASSES = (
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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
    'require_debug_false': {
        '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        'bongo': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

SUIT_CONFIG = {
    'ADMIN_NAME': SITE_NAME
}

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    os.path.normpath(os.path.join(BASE_DIR, 'templates')),
    os.path.normpath(os.path.join(BASE_DIR, 'apps/frontend/templates')),
)


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

### end drf ###

### django-cors-headers ###

CORS_ORIGIN_WHITELIST = (
    'bjacobel.com',
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

CELERY_ALWAYS_EAGER = False