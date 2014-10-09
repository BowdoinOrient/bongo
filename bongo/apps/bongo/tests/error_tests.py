from django.test import TestCase
from django.test import Client

class NotFoundTestCase(TestCase):
    def test_custom_404(self):
        client = Client()
        res = client.get("asdf")
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.templates[0].name, "custom404.html")
