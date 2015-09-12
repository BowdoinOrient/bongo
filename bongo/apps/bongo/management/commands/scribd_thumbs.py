from django.core.management.base import BaseCommand
from bongo.apps.bongo.models import Issue


class Command(BaseCommand):

    def handle(self, *args, **options):
        for issue in Issue.objects.all():
            issue.save()
