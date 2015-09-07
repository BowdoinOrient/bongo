from bongo.settings.prod import *

# The same settings as production, but no database password.

SECURE_SSL_REDIRECT = False

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
)

TEST_RUNNER = 'bongo.settings.tests.ReusableRunner'

HAYSTACK_CONNECTIONS['test'] = {
    'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
    'URL': 'http://127.0.0.1:9200/',
    'INDEX_NAME': 'haystack_test',
    'INCLUDE_SPELLING': True
}
