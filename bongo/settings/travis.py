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
}

INSTALLED_APPS += (
    'django_nose',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = ['--with-fixture-bundling', '--nologcapture']

NOSE_TESTMATCH = '(?:^|[b_./-])[Tt]ests'

RAVEN_CONFIG = {
    "dsn": "http://dd2c825ff9b1417d88a99573903ebf80:91631495b10b45f8a1cdbc492088da6a@localhost:9000/1",
}