from django.core.management.base import BaseCommand
from bongo.apps.bongo.models import Creator
from django.utils.html import strip_tags
import re

def cleaned(name):
    cl = name
    cl = strip_tags(cl)
    cl = cl.lower()

    cl = re.sub('&nbsp;', '', cl)

    if re.search(", the bowdoin orient", cl):
        cl = re.split(", the bowdoin orient", cl)[0]

    if re.search(", bowdoin orient", cl):
        cl = re.split(", bowdoin orient", cl)[0]

    if re.search("for the bowdoin orient", cl):
        cl = re.split("for the bowdoin orient", cl)[0]

    return cl

class Command(BaseCommand):

    def handle(self, *args, **options):
        """Authors exist multiple times in the database. This re-assigns dupe
        authors' content to the real author and 301s their author page.
        """

        for creator in Creator.objects.all():
            dupes = [creator]
            for potential_dupe in Creator.objects.exclude(pk=creator.pk):
                if cleaned(potential_dupe.name) == cleaned(creator.name):
                    dupes.append(potential_dupe)

            dupes = sorted(dupes, key=lambda x: len(x.works()))
            original = dupes.pop()

            for dupe in dupes:
                works = dupe.works()

                for work in works:
                    work.creators.remove(dupe)
                    work.creators.add(original)
                    work.save()

                dupe.dupe_of = original
                dupe.save()