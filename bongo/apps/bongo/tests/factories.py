import factory
from factory import fuzzy
from bongo.apps.bongo import models
from django.contrib.auth.models import User
from random import choice, sample, randint, jumpahead
from string import lowercase, digits, capitalize
from datetime import date, timedelta, datetime

class UserFactory(factory.Factory):
    class Meta:
        model = User

    first_name = factory.fuzzy.FuzzyText(chars=lowercase)
    last_name = factory.fuzzy.FuzzyText(chars=lowercase)
    username = factory.LazyAttribute(lambda obj: (obj.first_name[0] + obj.last_name).lower())
    email = factory.LazyAttribute(lambda obj: (obj.username + "@bowdoin.edu").lower())
    password = factory.PostGenerationMethodCall('set_password',
                                                'defaultpassword')

class JobFactory(factory.Factory):
    class Meta:
        model = models.Job

    title = factory.fuzzy.FuzzyChoice(["Editor in Chief", "Opinion Editor", "Contributor", "Staff Writer", "Columnist"])

class CreatorFactory(factory.Factory):
    class Meta:
        model = models.Creator

    user = factory.SubFactory(UserFactory)
    name = factory.fuzzy.FuzzyText(chars=lowercase)
    job = factory.SubFactory(JobFactory)
    twitter = factory.fuzzy.FuzzyText(prefix="@")
    profpic = factory.django.ImageField()

class TextFactory(factory.Factory):
    class Meta:
        model = models.Text

    caption = factory.Sequence(lambda n: 'This is text #{0}'.format(n))
    body = "It has a loooooooooooooong body"
    excerpt = "The excerpt isn't correct until it's saved"

class VideoFactory(factory.Factory):
    class Meta:
        model = models.Video

    caption = factory.Sequence(lambda n: 'This is video #{0}'.format(n))
    host = factory.fuzzy.FuzzyChoice(["Vimeo", "YouTube", "Vine"])
    uid = factory.fuzzy.FuzzyText()

class PDFFactory(factory.Factory):
    class Meta:
        model = models.PDF

    caption = factory.Sequence(lambda n: 'This is pdf #{0}'.format(n))

class PhotoFactory(factory.Factory):
    class Meta:
        model = models.Photo

    caption = factory.Sequence(lambda n: 'Photo #{0}'.format(n))
    staticfile = factory.django.ImageField(
        filename=factory.fuzzy.FuzzyText(chars=digits, suffix=".jpg").fuzz()
    )

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

    volume_number = factory.fuzzy.FuzzyInteger(1, 143)
    volume_year_start = factory.LazyAttribute(lambda obj: obj.volume_number+1870)
    volume_year_end = factory.LazyAttribute(lambda obj: obj.volume_number+1871)

class IssueFactory(factory.Factory):
    class Meta:
        model = models.Issue

    issue_date = factory.fuzzy.FuzzyDate(date(1871, 1, 1), date(1871, 1, 1) + timedelta(52560))
    issue_number = factory.fuzzy.FuzzyInteger(24)

    @factory.post_generation
    def idgaf(self, create, extracted, **kwargs):
        if create:
            v = VolumeFactory.create(); v.save()
            self.volume = v
            self.save()

class SectionFactory(factory.Factory):
    class Meta:
        model = models.Section

    section = factory.fuzzy.FuzzyChoice(["News","Features","A&E","Opinion","Sports"])
    priority = factory.fuzzy.FuzzyInteger(5)

class TagFactory(factory.Factory):
    class Meta:
        model = models.Tag

    tag = factory.fuzzy.FuzzyText(chars=lowercase)

class PostFactory(factory.Factory):
    class Meta:
        model = models.Post

    published = factory.fuzzy.FuzzyDate(date(1871, 1, 1), date(1871, 1, 1) + timedelta(52560))
    is_published = factory.fuzzy.FuzzyChoice([False, True])
    title = factory.fuzzy.FuzzyText(chars=lowercase)
    opinion = factory.fuzzy.FuzzyChoice([False, True])
    views_local = factory.fuzzy.FuzzyInteger(10000)
    views_global = factory.fuzzy.FuzzyInteger(10000)
    primary_type = factory.fuzzy.FuzzyChoice(["text","photo","video","liveblog","html","generic"])

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