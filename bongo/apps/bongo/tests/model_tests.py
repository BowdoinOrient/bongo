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

        # this is a damn good article. one of the best.
        articlebody = 'It\'s nerve-wracking enough to open the door at a party and find a security officer on the other side. Imagine opening that door naked. That\'s what happened at the first annual naked party in the spring of 2004, when Anna Troyansky \'06 answered the door for a female security officer. Consistent with the theme of the party, Troyansky was completely naked. The security officer simply asked, "Can you turn the music down?" "I remember peering around the door, reassuring them that we wouldturn the music down," Troyansky said. "I think they were surprised, aswell, to be greeted like that, but I don\'t think they realized at that point that there were another dozen naked people in the apartment. Who knows what crossed their minds." At the inaugural naked party, Troyansky was one of only 12 people at the party that could have opened the door and given Security something to look at besides an unregistered keg. Now, the annual Bowdoin naked party thrives, with attendance reaching almost 80 people at the largest party."Basically, it started with us waking up one morning and deciding not to wear clothes," said Brendan Mortimer \'06, who started Bowdoin\'s naked party tradition with Vanessa Lind \'06. "But, there were pragmatic problems. We couldn\'t really leave the apartment without clothes on. So, we thought, \'Why don\'t we just invite our friends over?\'"Mortimer and Lind, who were also inspired by friends who sometimes declared "naked time" in Quinby House, held their party in Mayflower Apartments the same night as Troyansky\'s underwear party. Since both parties were relatively small and the underwear partygoers were halfway to Mortimer and Lind\'s theme, they joined the naked party. "The proponents of the underwear party became the biggest proponents of the naked party," Lind said. "Parties tend to be pretty similar, and people love something novel in a party. It was an infectious thing, and everyone became more comfortable."Lind explained that while there was a core of naked partygoers, mainly Ultimate Frisbee players, the party grew because of curiosity. There were the first-timers, and there were those who failed to show up but heard the party talked about enough that they were convinced they had to make it to the next one.At the end of the spring 2006 semester, the entire senior class was invited to Mortimer and Lind\'s final naked party. "It added to the anticipation," Mortimer said. "People talked the most when they had gone the first time or when they missed it. It was exciting to see."At this year\'s annual naked party on November 11, partygoers, who asked to remain unnamed, agreed with Mortimer and Lind that after the initial five minutes, the nakedness was no longer awkward because everyone disrobed before entering the party and because there is an the acceptance of everyone\'s nakedness, regardless of body type. As a condition for reporting this story, the Orient agreed not to disclose the location of the party."What keeps it from being awkward? The fact that everyone\'s naked and they don\'t want people staring at their genitals, so they don\'t do it to other people," said one."When everyone\'s shown everything, there\'s no need to be awkward," Mortimer said. "Most people have the realization later in the night that, \'Hey, everyone\'s naked and it\'s been like that.\'" "I think a lot of people feel much more comfortable with and confident about their bodies and feel very liberated after attending a naked party," Troyansky added.The core of naked aficionados is accepting of newcomers and of all body types, stating that everyone embraces the diversity of the bodies walking through the door."There\'s a veteran community of naked people who welcome new participants without scrutinizing," one newcomer said. "They\'re actually very supportive, but not so supportive it\'s awkward."One partygoer\'s comments didn\'t even necessarily pertain to nudity: "The most interesting thing about naked parties is that tattoos start showing up so much. "Minus the grinding and clothes present at most college parties, the naked party is just like any other party. There\'s music, beer pong, and yes, even keg stands."Miraculous things happen," one partygoer said of people who are on the fence about attending the naked party. "People get drunk and start thinking, \'What would that be like?\'" When pressed further as to what "that" was, he answered that students\' curiosity often leads them to forgo their inhibitions and strip down. "You weren\'t curious when you came?" he asked. "You thought we might be cheating?" A naked party is a hard theme to fake, and one that demands total participation to make it work. One house resident, who wasn\'t in the main party area, was naked in his room doing schoolwork. "I\'m naked in spirit," he said. "And, well, I\'m actually naked. "A disrobing room outside the actual party made it so everyone kept the "no nudity, no entry" motto without freezing in the Maine weather. If it\'s difficult digging through coats in a crowd, it\'s hilarious digging through socks, shoes, boxers, and bras with five other people.For a good portion of the partygoers, it was their first foray into party nudity. But, because of the support and the acceptance of all body types, that foray wasn\'t as difficult as many initially believed. "There\'s always the next group that\'s convinced they have to go," Lind said, who has done interviews about the growing naked party trend for Canadian nudist magazine "Au Naturel" and "The Daily Free Press," Boston University\'s independent student newspaper. If nothing else, according to Lind, "Being naked is a good way to keep Security from coming because sometimes they just don\'t want to deal with the consequences." Just keep the music down and the clothes off.'
        post = factories.PostFactory.create()
        similar_post = factories.PostFactory.create()
        text = factories.TextFactory.create(body=articlebody)

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

    def test_primary_section(self):
        """Test that Series' primary_section method works"""

        series = factories.SeriesFactory.create()

        section1 = factories.SectionFactory.create()
        section2 = factories.SectionFactory.create()

        post1 = factories.PostFactory.create()
        post1.section = section1
        post1.series.add(series)
        post1.save()

        post2 = factories.PostFactory.create()
        post2.section = section2
        post2.series.add(series)
        post2.save()

        post3 = factories.PostFactory.create()
        post3.section = section2
        post3.series.add(series)
        post3.save()

        self.assertEqual(series.primary_section(), section2.classname())


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
