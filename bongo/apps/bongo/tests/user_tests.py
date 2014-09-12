from factories import *
from django.test import TestCase
from django.contrib.auth.models import User
from bongo.apps.bongo import models

class UserTestCase(TestCase):
    def test_password(self):
        """ Test that a user gets a password, and it works to log them in """

        user = UserFactory.build()
        self.assertNotEqual(user.password, u'')
        self.assertEqual(user.check_password("defaultpassword"), True)

class CreatorTestCase(TestCase):
    def test_foreign_key(self):
        """ Test that Creators are properly hooked up to Jobs and Users """

        user = UserFactory.build()
        creator = CreatorFactory.build()
        job = JobFactory.build()

        creator.user = user
        creator.job = job

        self.assertEquals(type(creator.user), User)
        self.assertEquals(type(creator.job), models.Job)

    def test_works(self):
        """ Test the connection between a creator and the content they've made """

        me = CreatorFactory.build()
        me.save()

        photo = PhotoFactory.build()
        photo.save()
        photo.creators.add(me)
        photo.save()

        video = VideoFactory.build()
        video.save()
        video.creators.add(me)
        video.save()

        self.assertIn(photo, me.works().all())
        self.assertIn(video, me.works().all())