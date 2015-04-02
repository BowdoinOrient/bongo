from django.test import TestCase
from rq import Queue
from rq_scheduler import Scheduler
from redis import Redis
from subprocess import Popen
from datetime import timedelta

def add(x, y):
    return x + y

class QueueTestCase(TestCase):
    def test_queued_code(self):
        """Test a simple queuing task with rq"""

        try:
            from subprocess import DEVNULL as devnull
        except ImportError:
            import os
            devnull = open(os.devnull, 'w')

        # make sure an rqworker is running
        rqworker = Popen("rqworker", shell=True, stdout=devnull, stderr=devnull, close_fds=True)

        q = Queue(connection=Redis())
        job = q.enqueue(add, 2, 2)

        while not job.result:
            pass

        try:
            self.assertEqual(add(2, 2), job.result)
        finally:
            # kill the rqworker, regardless of succcess
            rqworker.terminate()

    def test_scheduled_code(self):
        """Test scheduling something with rq-scheduler"""

        try:
            from subprocess import DEVNULL as devnull
        except ImportError:
            import os
            devnull = open(os.devnull, 'w')

        # make sure an rqworker is running
        rqworker = Popen("rqworker", shell=True, stdout=devnull, stderr=devnull, close_fds=True)

        s = Scheduler(connection=Redis())
        job = s.enqueue_in(timedelta(seconds=1))

        while not job.result:
            pass

        try:
            self.assertEqual(add(2, 2), job.result)
        finally:
            # kill the rqworker, regardless of succcess
            rqworker.terminate()