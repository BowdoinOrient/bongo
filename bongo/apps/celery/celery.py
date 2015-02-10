from __future__ import absolute_import
from datetime import timedelta
from celery import Celery, task
from django.conf import settings
from celery.schedules import crontab
import os

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bongo.settings.dev')

app = Celery('bongo.apps.celery')

try:
    if app.control.inspect().ping() != None:
        celery_is_running = True
    else:
        celery_is_running = False
except IOError:
    celery_is_running = False

app.conf.update(
    CELERY_TIMEZONE = settings.TIME_ZONE,
    CELERY_TASK_RESULT_EXPIRES = timedelta(hours=24),
    CELERY_CHORD_PROPAGATES = True,
    CELERY_RESULT_BACKEND='amqp',
    BROKER_URL=os.environ.get("RABBITMQ_BROKER_URL", ''),
    CELERY_ALWAYS_EAGER=(settings.CELERY_ALWAYS_EAGER and not celery_is_running),
    CELERY_EAGER_PROPAGATES_EXCEPTIONS = True,
    CELERYD_HIJACK_ROOT_LOGGER = True,
    CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml'],
    CELERY_TASK_SERIALIZER = 'json',
    CELERY_RESULT_SERIALIZER = 'json',
)

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

if hasattr(settings, 'RAVEN_CONFIG'):
    from raven import Client
    from raven.contrib.celery import register_signal
    client = Client(dsn=settings.RAVEN_CONFIG['dsn'])
    register_signal(client)

# Add scheduled tasks here.

app.conf.update(
    CELERYBEAT_SCHEDULE = {
        'every-day-amqp-clean': {
            'task': 'celery.backend_cleanup',
            'schedule': crontab(hour=4, minute=0)
        },
    }
)

# Add other tasks (testing, one-off) here.

@task(name='setup_tests.add', time_limit=1)
def add(x, y):
    logger = add.get_logger()
    logger.warn("result will be {}".format(x + y))
    return x + y