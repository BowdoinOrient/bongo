from django.test import TestCase
from rq import Queue
from redis import Redis
from subprocess import Popen

try:
    from subprocess import DEVNULL as devnull
except ImportError:
    from os import devnull  # fix for python < 3.3

def add(x, y):
    return x + y

class QueueTestCase(TestCase):
    def test_queued_code(self):
        # make sure an rqworker is running
        rqworker = Popen("rqworker", shell=True, stdout=devnull, stderr=devnull)

        q = Queue(connection=Redis())
        job = q.enqueue(add, 2, 2)

        while not job.result:
            pass

        try:
            self.assertEqual(add(2, 2), job.result)
        finally:
            # kill the rqworker, regardless of succcess
            rqworker.terminate()