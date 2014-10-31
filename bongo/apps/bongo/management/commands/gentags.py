from django.core.management.base import BaseCommand
from bongo.apps.bongo.models import Text
from bongo.apps.bongo.helpers import tagify

class Object:
    pass

class Command(BaseCommand):

    def handle(self, *args, **options):
        """ Generate tags for all existing articles. """
        for text in Text.objects.all():
            if text.post_set.all():
                post = text.post_set.all()[0]
            else:
                post = Object()
                post.title = "Undefined post"

            print "Suggested tags for post \"{}\":".format(post.title)
            print tagify(text.body)
            print ""