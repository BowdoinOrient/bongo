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
        scheduled_time=datetime.now(),
        func='haystack.management.commands.update_index.Command().handle()',
        interval=60 * 60,
        repeat=None,
    )

    for job in scheduler.get_jobs():
        index_job = job
        if index_job.func_name == 'haystack.management.commands.update_index.Command().handle()':
            break

    index_job.meta['task_type'] = "update_index"
    index_job.save()

task_list = [update_es_index]
