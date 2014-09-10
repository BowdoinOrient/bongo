from factories import *
from django.test import TestCase
from django.contrib.auth.models import User
from bongo.apps.bongo import models

class UserTestCase(TestCase):
    def test_password(self):
        user = UserFactory.build()
        self.assertNotEqual(user.password, u'')

class CreatorTestCase(TestCase):
    def test_foreign_key(self):
        user = UserFactory.build()
        creator = CreatorFactory.build()
        job = JobFactory.build()

        creator.user = user
        creator.job = job

        self.assertEquals(type(creator.user), User)
        self.assertEquals(type(creator.job), models.Job)