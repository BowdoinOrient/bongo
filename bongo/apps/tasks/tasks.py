from datetime import datetime
from rq_scheduler import Scheduler
from redis import Redis

scheduler = Scheduler(connection=Redis())

def update_es_index():
    """ Update the ElasticSearch index every hour."""

    for job in scheduler.get_jobs():
        if 'task_type' in job.meta and job.meta['task_type'] == "update_index":
            scheduler.cancel(job)

    scheduler.schedule(
        scheduled_time=datetime.now(),                                          # Time for first execution, in UTC timezone
        func='django.core.management.call_command("update_index --age=1")',     # Function to be queued
        interval=60*60,                                                         # Time before the function is called again, in seconds
        repeat=None,                                                            # Repeat this number of times (None means repeat forever)
    )

    for job in scheduler.get_jobs():
        index_job = job
        if index_job.func_name == 'django.core.management.call_command("update_index")':
            break

    index_job.meta['task_type'] = "update_index"
    index_job.save()

task_list = [update_es_index,]