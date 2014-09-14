from factories import *
from django.test import TestCase
from django.db import models

class SeriesTestCase(TestCase):
    def test_m2m(self):
        pass

class VolumeTestCase(TestCase):
    def test_foreign_key(self):
        pass

class IssueTestCase(TestCase):
    def test_foreign_key(self):
        pass

class SectionTestCase(TestCase):
    def test_foreign_key(self):
        pass

class TagTestCase(TestCase):
    def test_foreign_key(self):
        pass

    def test_autogen(self):
        pass
