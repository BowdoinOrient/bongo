from django.test import TestCase
from bongo.apps.bongo.tests import factories


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
