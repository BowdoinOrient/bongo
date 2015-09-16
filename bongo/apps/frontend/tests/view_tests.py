from django.test import TestCase
from bongo.apps.bongo.tests import factories
from datetime import datetime, timedelta


class ArticleViewTestCase(TestCase):
    def test_by_slug(self):
        """Test that you can route to an article by using its slug"""

        post = factories.PostFactory.create()

        response = self.client.get("/article/{}/".format(post.slug))
        self.assertEqual(response.status_code, 200)

    def test_by_id(self):
        """Test that you can route to an article by using its ID"""

        post = factories.PostFactory.create()

        response = self.client.get("/article/{}/".format(post.id))

        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.url, "http://testserver/article/{}/".format(post.slug))


class HomeViewTestCase(TestCase):
    pass


class AuthorViewTestCase(TestCase):
    pass


class SeriesViewTestCase(TestCase):
    def test_series_view_context(self):
        series = factories.SeriesFactory.create()
        posts = [factories.PostFactory.create() for x in range(5)]

        for post in posts:
            post.published = datetime.now() + timedelta(hours=post.pk)
            post.series.add(series)
            post.save(auto_dates=False)

        res = self.client.get('/series/{}/'.format(series.pk))

        self.assertEqual(series, res.context['series'])
        self.assertEqual(set(posts), set(res.context['posts']))

    def test_series_view_route(self):
        series = factories.SeriesFactory.create()

        self.assertEqual(self.client.get('/series/{}/'.format(series.pk)).status_code, 200)

        self.assertEqual(self.client.get('/series/'.format(series.pk)).status_code, 404)

        self.assertEqual(self.client.get('/series/0/').status_code, 404)


class StaticViewsTestCase(TestCase):
    def test_about_view(self):
        res = self.client.get('/about/')
        self.assertEqual(res.status_code, 200)

    def test_ethics_view(self):
        res = self.client.get('/ethics/')
        self.assertEqual(res.status_code, 200)

    def test_subscribe_view(self):
        res = self.client.get('/subscribe/')
        self.assertEqual(res.status_code, 200)

    def test_advertise_view(self):
        res = self.client.get('/advertise/')
        self.assertEqual(res.status_code, 200)

    def test_contact_view(self):
        res = self.client.get('/contact/')
        self.assertEqual(res.status_code, 200)
