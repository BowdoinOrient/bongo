from __future__ import absolute_import
from datetime import timedelta
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
import os

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bongo.settings.dev')

app = Celery('bongo.apps.celery')

app.conf.update(
    CELERY_TIMEZONE = settings.TIME_ZONE,
    CELERY_TASK_RESULT_EXPIRES = timedelta(hours=24),
    CELERY_CHORD_PROPAGATES = True,
    CELERY_RESULT_BACKEND='amqp',
    BROKER_URL=os.environ.get("RABBITMQ_BROKER_URL", 'amqp://guest@localhost'),
    CELERY_ALWAYS_EAGER=True if settings.CELERY_ALWAYS_EAGER and app.control.inspect().ping() == None else False,
    CELERY_EAGER_PROPAGATES_EXCEPTIONS = True,
    CELERYD_HIJACK_ROOT_LOGGER = False
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
