from bongo.settings.prod import *

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
}

INSTALLED_APPS += (
    'django_nose',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = ['--with-fixture-bundling', '--nologcapture', '--verbosity=2']

NOSE_TESTMATCH = '(?:^|[b_./-])[Tt]ests'