from django.test import TestCase
from django.test.utils import override_settings
from celery import task

@task()
def add(x, y):
    return x + y

class TaskTestCase(TestCase):
    def test_add_task(self):
        """ Test a simple delayed task to make sure Celery is working """
        result = add.delay(8, 8)
        self.assertEquals(result.get(), 16)
        self.assertTrue(result.successful())