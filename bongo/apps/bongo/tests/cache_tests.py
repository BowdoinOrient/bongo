from django.test import TestCase
from django.core.cache import cache


class CacheTestCase(TestCase):
    def test_cache_task(self):
        """ Test memcached or LocMemCache, just so we know it's working """
        cached = cache.get("cache_key")

        if not cached:
            cache.set("cache_key", "cache_value", 30)

        self.assertEqual(cache.get("cache_key"), "cache_value")
