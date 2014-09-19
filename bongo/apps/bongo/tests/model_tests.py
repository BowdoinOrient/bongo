from factories import *
from django.test import TestCase
from django.contrib.auth.models import User

"""
Test content type models and related:
test, video, PDF, photo, HTML, pullquote, post
"""

class TextTestCase(TestCase):
    def test_creator(self):
        text = TextFactory.build(); text.save()

        creator1 = CreatorFactory.build(); creator1.save()
        creator2 = CreatorFactory.build(); creator2.save()

        text.creators.add(creator1)
        text.creators.add(creator2)
        text.save()

        for creator in text.creators.all():
            self.assertIn(text, creator.works())

        for creator in [creator1, creator2]:
            self.assertIn(text, creator.works())

        text.delete()
        creator1.delete()
        creator2.delete()

    def test_fields(self):
        text = TextFactory.build()
        self.assertIsNotNone(text.caption)

    def test_excerpt(self):
        text = TextFactory.build()
        self.assertEquals(text.excerpt, "The excerpt isn't correct until it's saved")
        text.body = "Quinoa hashtag Kickstarter bespoke. Schlitz PBR&B 3 wolf moon, photo booth swag occupy banh mi PBR artisan lo-fi normcore. Lomo selvage leggings quinoa, ugh cliche cornhole asymmetrical gluten-free Echo Park. Tumblr put a bird on it drinking vinegar sriracha, leggings mumblecore actually four loko twee fixie mustache. Mustache drinking vinegar cliche, meggings before they sold out fap Kickstarter tofu banjo master cleanse ennui fingerstache kogi you probably haven't heard of them. Polaroid photo booth chia biodiesel trust fund typewriter locavore, Blue Bottle 90's Neutra umami flannel. Portland Helvetica umami freegan locavore direct trade, polaroid 3 wolf moon actually."
        text.save()
        self.assertEquals(text.excerpt, "Quinoa hashtag Kickstarter bespoke. Schlitz PBR&B 3 wolf moon, photo booth swag occupy banh mi PBR artisan lo-fi normcore. Lomo selvage leggings quinoa, ugh cliche cornhole asymmetrical gluten-free Echo Park.")
        text.delete()

class VideoTestCase(TestCase):
    def test_creator(self):
        video = VideoFactory.build(); video.save()

        creator1 = CreatorFactory.build(); creator1.save()
        creator2 = CreatorFactory.build(); creator2.save()

        video.creators.add(creator1)
        video.creators.add(creator2)
        video.save()

        for creator in video.creators.all():
            self.assertIn(video, creator.works())

        for creator in [creator1, creator2]:
            self.assertIn(video, creator.works())

        video.delete()
        creator1.delete()
        creator2.delete()

    def test_fields(self):
        video = VideoFactory.build()
        self.assertIsNotNone(video.caption)
        self.assertIsNotNone(video.url())


class PDFTestCase(TestCase):
    def test_creator(self):
        pdf = PDFFactory.build(); pdf.save()

        creator1 = CreatorFactory.build(); creator1.save()
        creator2 = CreatorFactory.build(); creator2.save()

        pdf.creators.add(creator1)
        pdf.creators.add(creator2)
        pdf.save()

        for creator in pdf.creators.all():
            self.assertIn(pdf, creator.works())

        for creator in [creator1, creator2]:
            self.assertIn(pdf, creator.works())

        pdf.delete()
        creator1.delete()
        creator2.delete()

    def test_fields(self):
        pdf = PDFFactory.build()
        self.assertIsNotNone(pdf.caption)
        # @todo: test staticfile


class PhotoTestCase(TestCase):
    def test_creator(self):
        photo = PhotoFactory.build(); photo.save()

        creator1 = CreatorFactory.build(); creator1.save()
        creator2 = CreatorFactory.build(); creator2.save()

        photo.creators.add(creator1)
        photo.creators.add(creator2)
        photo.save()

        for creator in photo.creators.all():
            self.assertIn(photo, creator.works())

        for creator in [creator1, creator2]:
            self.assertIn(photo, creator.works())

        photo.delete()
        creator1.delete()
        creator2.delete()

    def test_fields(self):
        photo = PhotoFactory.build()
        self.assertIsNotNone(photo.caption)
        # @todo: test staticfile


class HTMLTestCase(TestCase):
    def test_creator(self):
        html = HTMLFactory.build(); html.save()

        creator1 = CreatorFactory.build(); creator1.save()
        creator2 = CreatorFactory.build(); creator2.save()

        html.creators.add(creator1)
        html.creators.add(creator2)
        html.save()

        for creator in html.creators.all():
            self.assertIn(html, creator.works())

        for creator in [creator1, creator2]:
            self.assertIn(html, creator.works())

        html.delete()
        creator1.delete()
        creator2.delete()

    def test_fields(self):
        html = HTMLFactory.build()
        self.assertIsNotNone(html.caption)
        self.assertIsNotNone(html.content)


class PullquoteTestCase(TestCase):
    def test_creator(self):
        pullquote = PullquoteFactory.build(); pullquote.save()

        creator1 = CreatorFactory.build(); creator1.save()
        creator2 = CreatorFactory.build(); creator2.save()

        pullquote.creators.add(creator1)
        pullquote.creators.add(creator2)
        pullquote.save()

        for creator in pullquote.creators.all():
            self.assertIn(pullquote, creator.works())

        for creator in [creator1, creator2]:
            self.assertIn(pullquote, creator.works())

        pullquote.delete()
        creator1.delete()
        creator2.delete()

    def test_fields(self):
        pullquote = PullquoteFactory.build()
        self.assertIsNotNone(pullquote.caption)
        self.assertIsNotNone(pullquote.quote)
        self.assertIsNotNone(pullquote.attribution)

class PostTestCase(TestCase):
    pass

"""
Test user-related models:
creators, users, jobs
"""

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

        creator.save()

        self.assertEquals(type(creator.user), User)
        from bongo.apps.bongo.models import Job
        self.assertEquals(type(creator.job), Job)

        creator.delete()

    def test_works(self):
        """ Test the connection between a creator and the content they've made """

        me = CreatorFactory.build(); me.save()

        photo = PhotoFactory.build(); photo.save()
        photo.creators.add(me)
        photo.save()

        video = VideoFactory.build(); video.save()
        video.creators.add(me)
        video.save()

        self.assertIn(photo, me.works())
        self.assertIn(video, me.works())

        me.delete()
        photo.delete()
        video.delete()

class JobTestCase(TestCase):
    def test_foreign_key(self):
        job = JobFactory.build(); job.save()
        creator = CreatorFactory.build(); creator.save()
        creator.job = job
        creator.save()

        self.assertEqual(job, creator.job)
        self.assertIn(creator, job.workers())

        job.delete()
        creator.delete()

"""
Test metadata models:
series, volumes, issues, sections, tags
"""

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
