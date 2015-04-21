from django.test import TestCase, Client
from bongo.apps.bongo.models import Creator, Series, Post
from bongo.apps.bongo.tests.factories import CreatorFactory, SeriesFactory, PostFactory
from haystack.query import SearchQuerySet
from django.core import management, urlresolvers

class SearchTestCase(TestCase):
    def test_creator_search(self):
        """Assert that you can find Creators via search"""

        obj = CreatorFactory.create()

        management.call_command('update_index', verbosity=0, interactive=False)

        sqs = SearchQuerySet().all()
        res = sqs.auto_query(obj.name)

        self.assertGreater(len(res), 0)
        self.assertIn(Creator.objects.filter(pk__exact=obj.pk).first(), [res_item.object for res_item in res])

    def test_series_search(self):
        """Assert that you can find Series via search"""

        obj = SeriesFactory.create()

        management.call_command('update_index', verbosity=0, interactive=False)

        sqs = SearchQuerySet().all()
        res = sqs.auto_query(obj.name)


        self.assertGreater(len(res), 0)
        self.assertIn(Series.objects.filter(pk__exact=obj.pk).first(), [res_item.object for res_item in res])

    def test_article_search(self):
        """Assert that you can find Articles via search"""

        obj = PostFactory.create()

        management.call_command('update_index', verbosity=0, interactive=False)

        sqs = SearchQuerySet().all()
        res = sqs.auto_query(obj.text.all()[0].body[:100])

        self.assertGreater(len(res), 0)
        self.assertIn(Post.objects.filter(pk__exact=obj.pk).first(), [res_item.object for res_item in res])

    def test_search_view(self):
        """Test that you can search by querying the search page"""
        c = Client()

        obj = CreatorFactory.create()
        management.call_command('update_index', verbosity=0, interactive=False)

        res = c.get(urlresolvers.reverse("haystack_search"), {"q": obj.name})

        self.assertGreater(len(res.context['page'].object_list), 0)
        self.assertEqual(res.context['page'].object_list[0].object, obj)