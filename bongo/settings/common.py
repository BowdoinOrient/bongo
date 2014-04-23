"""
Django settings for bongo project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os
from datetime import timedelta
from djcelery import setup_loader


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

    # Suit has to come before contrib.admin
    'suit',
    'django.contrib.admin',

    # Asynchronous task queue:
    'djcelery',

    # Local apps
    'bongo.apps.bongo',
    'bongo.apps.archive',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'bongo.urls'

WSGI_APPLICATION = 'bongo.wsgi.application'


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

STATIC_URL ='/static/'
STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'static'))

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Brian Jacobel', 'bjacobel@bowdoin.edu'),
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
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

########## CELERY CONFIGURATION
# See: http://celery.readthedocs.org/en/latest/configuration.html#celery-task-result-expires
CELERY_TASK_RESULT_EXPIRES = timedelta(minutes=30)

# See: http://docs.celeryproject.org/en/master/configuration.html#std:setting-CELERY_CHORD_PROPAGATES
CELERY_CHORD_PROPAGATES = True

# See: http://celery.github.com/celery/django/
setup_loader()

CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"

CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'

BROKER_URL='amqp://localhost'

CELERY_ACCEPT_CONTENT = []  # make Celery shut up about deprecation
########## END CELERY CONFIGURATION

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
)
