from django.test import TestCase
from django.conf import settings
from django.template import Context, Template
from bongo.apps.bongo.tests import factories


def render_template(string, context=None):
    context = Context(context) if context else None
    return Template(string).render(context)


class TemplateTagsTestCase(TestCase):
    def test_dump_templatetag(self):
        """Test the dump() template tag (print object representation)"""
        article = factories.PostFactory.create()

        rendered = render_template(
            "{% load dump %}{{ article | dump }}",
            context = {
                "article": article
            }
        )

        self.assertEqual(rendered, article.__dict__)

    def test_dump_templatetag(self):
        """Test the class_name() template tag (print object's class name)"""
        article = factories.PostFactory.create()

        rendered = render_template(
            "{% load class_name %}{{ article | class_name }}",
            context = {
                "article": article
            }
        )

        self.assertEqual(rendered, "Post")
