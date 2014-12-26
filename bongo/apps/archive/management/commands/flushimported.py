from django.core.management.base import BaseCommand
from django.db import models as registered_models

class Command(BaseCommand):

    def handle(self, *args, **options):
        for model in registered_models.get_models(include_auto_created=True):
            if model._meta.app_label == "bongo":
                for obj in model.objects.all():
                    if obj.imported:
                        obj.delete()