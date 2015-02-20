from bongo.apps.bongo.tests import factories
from django.test import TestCase
from django.contrib.auth.models import User

"""
Test content type models and related:
test, video, PDF, photo, HTML, pullquote, post
"""

class TextTestCase(TestCase):
    def test_creator(self):
        text = factories.TextFactory.create()

        creator1 = factories.CreatorFactory.create()
        creator2 = factories.CreatorFactory.create()

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
        text = factories.TextFactory.create()
        self.assertIsNotNone(text.caption)

    def test_excerpt(self):
        text = factories.TextFactory.build()
        self.assertEquals(text.excerpt, "The excerpt isn't correct until it's saved")
        text.body = "Quinoa hashtag Kickstarter bespoke. Schlitz PBR&B 3 wolf moon, photo booth swag occupy banh mi PBR artisan lo-fi nor.bongo. Lomo selvage leggings quinoa, ugh cliche cornhole asymmetrical gluten-free Echo Park. Tumblr put a bird on it drinking vinegar sriracha, leggings mumbl.bongo actually four loko twee fixie mustache. Mustache drinking vinegar cliche, meggings before they sold out fap Kickstarter tofu banjo master cleanse ennui fingerstache kogi you probably haven't heard of them. Polaroid photo booth chia biodiesel trust fund typewriter locavore, Blue Bottle 90's Neutra umami flannel. Portland Helvetica umami freegan locavore direct trade, polaroid 3 wolf moon actually."
        text.save()
        self.assertEquals(text.excerpt, "Quinoa hashtag Kickstarter bespoke. Schlitz PBR&B 3 wolf moon, photo booth swag occupy banh mi PBR artisan lo-fi nor.bongo. Lomo selvage leggings quinoa, ugh cliche cornhole asymmetrical gluten-free Echo Park.")
        text.delete()

class VideoTestCase(TestCase):
    def test_creator(self):
        video = factories.VideoFactory.create()

        creator1 = factories.CreatorFactory.create()
        creator2 = factories.CreatorFactory.create()

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
        video = factories.VideoFactory.build()
        self.assertIsNotNone(video.caption)
        self.assertIsNotNone(video.url())


class PDFTestCase(TestCase):
    def test_creator(self):
        pdf = factories.PDFFactory.create()

        creator1 = factories.CreatorFactory.create()
        creator2 = factories.CreatorFactory.create()

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
        pdf = factories.PDFFactory.create()
        self.assertIsNotNone(pdf.caption)
        # @todo: test staticfile


class PhotoTestCase(TestCase):
    def test_creator(self):
        photo = factories.PhotoFactory.create()

        creator1 = factories.CreatorFactory.create()
        creator2 = factories.CreatorFactory.create()

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
        photo = factories.PhotoFactory.create()
        self.assertIsNotNone(photo.caption)
        # @todo: test staticfile


class HTMLTestCase(TestCase):
    def test_creator(self):
        html = factories.HTMLFactory.create()

        creator1 = factories.CreatorFactory.create()
        creator2 = factories.CreatorFactory.create()

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
        html = factories.HTMLFactory.create()
        self.assertIsNotNone(html.caption)
        self.assertIsNotNone(html.content)


class PullquoteTestCase(TestCase):
    def test_creator(self):
        pullquote = factories.PullquoteFactory.create()

        creator1 = factories.CreatorFactory.create()
        creator2 = factories.CreatorFactory.create()

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
        pullquote = factories.PullquoteFactory.create()
        self.assertIsNotNone(pullquote.caption)
        self.assertIsNotNone(pullquote.quote)
        self.assertIsNotNone(pullquote.attribution)


class PostTestCase(TestCase):
    def test_similar_tags(self):

        hurrdurr = "What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo."
        post = factories.PostFactory.create()
        similar_post = factories.PostFactory.create()
        text = factories.TextFactory.create(body=hurrdurr)

        post.text.add(text)
        post.save()

        similar_post.text.add(text)
        similar_post.save()

        post.taggit()
        similar_post.taggit()

        self.assertNotEqual(post.tags.all().count(), 0)
        self.assertNotEqual(similar_post.tags.all().count(), 0)

        self.assertEqual(post.similar_tags()[0], similar_post)

    def test_popularity(self):
        post1 = factories.PostFactory.create(); post1.views_global = 1
        post2 = factories.PostFactory.create(); post2.views_global = 2
        post3 = factories.PostFactory.create(); post3.views_global = 3

        self.assertGreater(post2.popularity(), post1.popularity())
        self.assertGreater(post3.popularity(), post2.popularity())


"""
Test user-related models:
creators, users, jobs
"""

class UserTestCase(TestCase):
    def test_password(self):
        """ Test that a user gets a password, and it works to log them in """

        user = factories.UserFactory.create()
        self.assertNotEqual(user.password, u'')
        self.assertEqual(user.check_password("defaultpassword"), True)

class CreatorTestCase(TestCase):
    def test_foreign_key(self):
        """ Test that Creators are properly hooked up to Jobs and Users """

        user = factories.UserFactory.create()
        creator = factories.CreatorFactory.create()
        job = factories.JobFactory.create()

        creator.user = user
        creator.job = job

        creator.save()

        self.assertEquals(type(creator.user), User)
        from bongo.apps.bongo.models import Job
        self.assertEquals(type(creator.job), Job)

        creator.delete()

    def test_works(self):
        """ Test the connection between a creator and the content they've made """

        me = factories.CreatorFactory.create()

        photo = factories.PhotoFactory.create()
        photo.creators.add(me)
        photo.save()

        video = factories.VideoFactory.create()
        video.creators.add(me)
        video.save()

        self.assertIn(photo, me.works())
        self.assertIn(video, me.works())

        me.delete()
        photo.delete()
        video.delete()

class JobTestCase(TestCase):
    def test_foreign_key(self):
        job = factories.JobFactory.create()
        creator = factories.CreatorFactory.create()
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
        # @TODO
        pass

class VolumeTestCase(TestCase):
    def test_foreign_key(self):
        # @TODO
        pass

class IssueTestCase(TestCase):
    def test_foreign_key(self):
        # @TODO
        pass

    def test_custom_save(self):
        issue = factories.IssueFactory.create(
            volume = factories.VolumeFactory.create()
        )
        self.assertEqual(issue.scribd, None)
        self.assertEqual(issue.scribd_image, None)
        issue.scribd = 99999999
        issue.save()
        self.assertEqual(issue.scribd_image, None)
        issue.scribd = 201901393
        issue.save()
        self.assertEqual(issue.scribd_image[:8], "https://")


class SectionTestCase(TestCase):
    def test_foreign_key(self):
        # @TODO
        pass

    def test_shortname(self):
        section = factories.SectionFactory.create()
        self.assertLess(len(section.classname()), 9)
        self.assertEqual(section.classname(), section.classname().lower())

class TagTestCase(TestCase):
    def test_foreign_key(self):
        # @TODO
        pass

    def test_autogen(self):
        # @TODO
        pass
