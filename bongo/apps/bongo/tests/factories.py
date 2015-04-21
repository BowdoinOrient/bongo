import factory
from factory.django import DjangoModelFactory as Factory
from faker import Faker
from bongo.apps.bongo import models
from django.contrib.auth.models import User
from django.utils.timezone import make_aware
from django.conf import settings
from random import choice
from string import ascii_lowercase as lowercase, digits
from datetime import date, timedelta, datetime
import pytz

tz = pytz.timezone(settings.TIME_ZONE)

fake = Faker()

class UserFactory(Factory):
    class Meta:
        model = User

    first_name = factory.LazyAttribute(lambda x: fake.first_name())
    last_name = factory.LazyAttribute(lambda x: fake.last_name())
    username = factory.LazyAttribute(lambda obj: (obj.first_name[0] + obj.last_name).lower())
    email = factory.LazyAttribute(lambda obj: (obj.username + "@bowdoin.edu").lower())
    password = factory.PostGenerationMethodCall('set_password',
                                                'defaultpassword')

class JobFactory(Factory):
    class Meta:
        model = models.Job

    title = choice(["Editor in Chief", "Opinion Editor", "Contributor", "Staff Writer", "Columnist"])

class CreatorFactory(Factory):
    class Meta:
        model = models.Creator

    user = factory.SubFactory(UserFactory)
    name = factory.LazyAttribute(lambda x: fake.name())
    job = factory.SubFactory(JobFactory)
    twitter = "@"+''.join(choice(lowercase) for i in range(8))
    profpic = factory.django.ImageField()

class TextFactory(Factory):
    class Meta:
        model = models.Text

    caption = factory.Sequence(lambda n: 'This is text #{0}'.format(n))
    body = fake.text(max_nb_chars=3000)
    excerpt = "The excerpt isn't correct until it's saved"

class VideoFactory(Factory):
    class Meta:
        model = models.Video

    caption = factory.Sequence(lambda n: 'This is video #{0}'.format(n))
    host = choice(["Vimeo", "YouTube", "Vine"])
    uid = ''.join(choice(lowercase + digits) for i in range(15))

class PDFFactory(Factory):
    class Meta:
        model = models.PDF

    caption = factory.Sequence(lambda n: 'This is pdf #{0}'.format(n))

class PhotoFactory(Factory):
    class Meta:
        model = models.Photo

    caption = factory.Sequence(lambda n: 'This is photo #{0}'.format(n))
    staticfile = factory.django.ImageField()

class HTMLFactory(Factory):
    class Meta:
        model = models.HTML

    caption = factory.Sequence(lambda n: 'This is html #{0}'.format(n))
    content = "<script type='text/javascript'>alert('lol xss');</script>"

class PullquoteFactory(Factory):
    class Meta:
        model = models.Pullquote

    caption = factory.Sequence(lambda n: 'This is pullquote #{0}'.format(n))
    quote = "Success is my only motherfuckin' option, failure's not"
    attribution = "Marshall Mathers, TDD evangelist"

class SeriesFactory(Factory):
    class Meta:
        model = models.Series

    name = factory.Sequence(lambda n: 'super punny series name #{0}'.format(n))

class VolumeFactory(Factory):
    class Meta:
        model = models.Volume

    volume_number = choice(range(143))+1
    volume_year_start = factory.LazyAttribute(lambda obj: obj.volume_number+1870)
    volume_year_end = factory.LazyAttribute(lambda obj: obj.volume_number+1871)

class IssueFactory(Factory):
    class Meta:
        model = models.Issue

    issue_date = date(1871, 1, 1) + timedelta(52560)
    issue_number = choice(range(24))
    volume = factory.SubFactory(VolumeFactory)

class SectionFactory(Factory):
    class Meta:
        model = models.Section

    section = choice(["News","Features","A&E","Opinion","Sports"])
    priority = choice(range(5))

class TagFactory(Factory):
    class Meta:
        model = models.Tag

    tag = ''.join(choice(lowercase) for i in range(10))

class PostFactory(Factory):
    class Meta:
        model = models.Post

    published = make_aware(datetime(1871, 1, 1) + timedelta(52560), tz)
    is_published = choice([False, True])
    title = factory.LazyAttribute(lambda x: u''.join(choice(lowercase+" ") for i in range(20)))
    opinion = choice([False, True])
    views_local = choice(range(0,10000))
    views_global = choice(range(0,10000))
    primary_type = choice(["text","photo","video","liveblog","html","generic"])

    volume = factory.SubFactory(VolumeFactory)
    issue = factory.SubFactory(IssueFactory)
    section = factory.SubFactory(SectionFactory)

    @factory.post_generation
    def content(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        self.text.add(TextFactory.create())
        self.video.add(VideoFactory.create())
        self.text.add(TextFactory.create())
        self.pdf.add(PDFFactory.create())
        self.photo.add(PhotoFactory.create())
        self.html.add(HTMLFactory.create())
        self.pullquote.add(PullquoteFactory.create())