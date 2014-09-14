from prod import *

# The same settings as production, but no database password.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bongo_test',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
    'archive': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DB02Orient_test',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

INSTALLED_APPS += (
    'django_nose',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = ['--with-fixture-bundling']

NOSE_TESTMATCH = '(?:^|[b_./-])[Tt]ests'