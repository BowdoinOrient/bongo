from django.test import TestCase
from bongo.apps.bongo.helpers import tagify
from django.conf import settings
import os

# This is the real article as it's represented in the database (woof)
with open(os.path.normpath(os.path.join(settings.SITE_ROOT, "bongo/apps/bongo/tests/naked.html")), "r") as f_html:
    articlehtml = f_html.read()

# This is a version I cleaned up by hand
with open(os.path.normpath(os.path.join(settings.SITE_ROOT, "bongo/apps/bongo/tests/naked.txt")), "r") as f_txt:
    articletext = f_txt.read()


class TaggerTestCase(TestCase):
    def test_tagify(self):
        """Test that tagify() can reproducibly find good tags for an article

        Furthermore, test that the tags are chosen irrelevant of HTML in the article
        """

        self.assertEqual(len(tagify(articletext)), 5)

        self.assertEqual(len(tagify(articlehtml)), 5)

        self.assertEqual(tagify(articlehtml), tagify(articletext))
