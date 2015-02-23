from django.test import TestCase
from bongo.apps.celery.celery import add

class TaskTestCase(TestCase):
    def test_add_task(self):
        """ Test a simple delayed task to make sure Celery is working """
        result = add.delay(8, 8)
        self.assertEquals(result.get(), 16)
        self.assertTrue(result.successful())