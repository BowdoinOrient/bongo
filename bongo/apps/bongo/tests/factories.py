import factory
from faker import Faker
from bongo.apps.bongo import models
from django.contrib.auth.models import User
from random import choice, sample, randint
from string import lowercase, digits, capitalize
from datetime import date, timedelta, datetime

fake = Faker()

class UserFactory(factory.Factory):
    class Meta:
        model = User

    first_name = factory.LazyAttribute(lambda x: fake.first_name())
    last_name = factory.LazyAttribute(lambda x: fake.last_name())
    username = factory.LazyAttribute(lambda obj: (obj.first_name[0] + obj.last_name).lower())
    email = factory.LazyAttribute(lambda obj: (obj.username + "@bowdoin.edu").lower())
    password = factory.PostGenerationMethodCall('set_password',
                                                'defaultpassword')

class JobFactory(factory.Factory):
    class Meta:
        model = models.Job

    title = choice(["Editor in Chief", "Opinion Editor", "Contributor", "Staff Writer", "Columnist"])

class CreatorFactory(factory.Factory):
    class Meta:
        model = models.Creator

    user = factory.SubFactory(UserFactory)
    name = factory.LazyAttribute(lambda x: fake.name())
    job = factory.SubFactory(JobFactory)
    twitter = "@"+''.join(choice(lowercase) for i in range(8))
    profpic = factory.django.ImageField()

class TextFactory(factory.Factory):
    class Meta:
        model = models.Text

    caption = factory.Sequence(lambda n: 'This is text #{0}'.format(n))
    body = fake.text(max_nb_chars=1000)
    excerpt = "The excerpt isn't correct until it's saved"

class VideoFactory(factory.Factory):
    class Meta:
        model = models.Video

    caption = factory.Sequence(lambda n: 'This is video #{0}'.format(n))
    host = choice(["Vimeo", "YouTube", "Vine"])
    uid = ''.join(choice(lowercase + digits) for i in range(15))

class PDFFactory(factory.Factory):
    class Meta:
        model = models.PDF

    caption = factory.Sequence(lambda n: 'This is pdf #{0}'.format(n))

class PhotoFactory(factory.Factory):
    class Meta:
        model = models.Photo

    caption = factory.Sequence(lambda n: 'This is photo #{0}'.format(n))
    staticfile = factory.django.ImageField()

class HTMLFactory(factory.Factory):
    class Meta:
        model = models.HTML

    caption = factory.Sequence(lambda n: 'This is html #{0}'.format(n))
    content = "<script type='text/javascript'>alert('lol xss');</script>"

class PullquoteFactory(factory.Factory):
    class Meta:
        model = models.Pullquote

    caption = factory.Sequence(lambda n: 'This is pullquote #{0}'.format(n))
    quote = "Success is my only motherfuckin' option, failure's not"
    attribution = "Marshall Mathers, TDD evangelist"

class SeriesFactory(factory.Factory):
    class Meta:
        model = models.Series

    name = factory.Sequence(lambda n: 'super punny series name #{0}'.format(n))

class VolumeFactory(factory.Factory):
    class Meta:
        model = models.Volume

    volume_number = choice(range(143))+1
    volume_year_start = factory.LazyAttribute(lambda obj: obj.volume_number+1870)
    volume_year_end = factory.LazyAttribute(lambda obj: obj.volume_number+1871)

class IssueFactory(factory.Factory):
    class Meta:
        model = models.Issue

    issue_date = date(1871, 1, 1) + timedelta(52560)
    issue_number = choice(range(24))

    @factory.post_generation
    def idgaf(self, create, extracted, **kwargs):
        if create:
            v = VolumeFactory.create(); v.save()
            self.volume = v
            self.save()

class SectionFactory(factory.Factory):
    class Meta:
        model = models.Section

    section = choice(["News","Features","A&E","Opinion","Sports"])
    priority = choice(range(5))

class TagFactory(factory.Factory):
    class Meta:
        model = models.Tag

    tag = ''.join(choice(lowercase) for i in range(10))

class PostFactory(factory.Factory):
    class Meta:
        model = models.Post

    published = datetime(1871, 1, 1) + timedelta(52560)
    is_published = choice([False, True])
    title = factory.LazyAttribute(lambda x: u''.join(choice(lowercase+" ") for i in range(20)))
    opinion = choice([False, True])
    views_local = choice(range(0,10000))
    views_global = choice(range(0,10000))
    primary_type = choice(["text","photo","video","liveblog","html","generic"])

    @factory.post_generation
    def idgaf(self, create, extracted, **kwargs):
        if create:
            v = VolumeFactory.create(); v.save()
            i = IssueFactory.create(); i.save()
            s = SectionFactory.create(); s.save()
            self.volume = v
            self.issue = i
            self.section = s
            self.save()