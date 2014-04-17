# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


""" Have been imported """
class Ads(models.Model):
    id = models.AutoField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    sponsor = models.CharField(max_length=100)
    link = models.CharField(max_length=100, blank=True)
    filename = models.CharField(max_length=100)
    type = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'ads'


""" Have been imported """
class Alerts(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField()
    urgent = models.IntegerField()
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'alerts'


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    volume = models.IntegerField()
    issue_number = models.IntegerField()
    section_id = models.IntegerField()
    priority = models.IntegerField()
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    excerpt = models.TextField()
    series = models.IntegerField()
    type = models.IntegerField()
    views = models.IntegerField()
    views_bowdoin = models.IntegerField()
    published = models.IntegerField()
    featured = models.IntegerField()
    longform = models.IntegerField()
    opinion = models.IntegerField()
    bigphoto = models.IntegerField()
    active = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()
    date_created = models.DateTimeField()
    date_published = models.DateTimeField()
    date_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article'

""" Won't import this: was an in-place JOIN between Articles, Authors and Jobs.
Good example of something Toph architected really well, but superceded now.
"""
class Articleauthor(models.Model):
    id = models.AutoField(primary_key=True)
    article_id = models.IntegerField()
    author_id = models.IntegerField()
    job_id = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'articleauthor'


class Articlebody(models.Model):
    id = models.AutoField(primary_key=True)
    article_id = models.IntegerField()
    body = models.TextField()
    active = models.IntegerField()
    timestamp = models.DateTimeField()
    creator_id = models.IntegerField(blank=True, null=True)
    major = models.IntegerField()
    comment = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'articlebody'

""" Won't import this """
class Articletype(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'articletype'


class Attachments(models.Model):
    id = models.AutoField(primary_key=True)
    article_id = models.IntegerField(blank=True, null=True)
    author_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=100, blank=True)
    content1 = models.TextField(blank=True)
    content2 = models.TextField(blank=True)
    big = models.IntegerField()
    active = models.IntegerField()
    afterpar = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attachments'


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    photo = models.CharField(max_length=150, blank=True)
    job = models.IntegerField()
    bio = models.TextField(blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'author'

""" Won't import this """
class Browse(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'browse'

""" Won't import this """
class CiSessions(models.Model):
    session_id = models.CharField(primary_key=True, max_length=40)
    ip_address = models.CharField(max_length=16)
    user_agent = models.CharField(max_length=120)
    last_activity = models.IntegerField()
    user_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'ci_sessions'

""" Won't import this """
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    article_id = models.IntegerField(blank=True, null=True)
    article_date = models.DateField()
    article_section = models.IntegerField()
    article_priority = models.IntegerField()
    username = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    comment = models.TextField()
    deleted = models.CharField(max_length=1)
    secret = models.IntegerField()
    comment_date = models.DateTimeField()
    realname = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'comment'

""" Won't import this """
class Event(models.Model):
    issue_date = models.DateField()
    event_date = models.DateField()
    event_priority = models.IntegerField()
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    timeplace = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'event'

""" Has been imported """
class Issue(models.Model):
    id = models.AutoField(primary_key=True)
    issue_date = models.DateField()
    volume = models.IntegerField()
    issue_number = models.IntegerField()
    ready = models.IntegerField()
    scribd = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'issue'


class Job(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'job'

""" Won't import this """
class Links(models.Model):
    id = models.AutoField(primary_key=True)
    article_id = models.IntegerField()
    article_date = models.DateField()
    article_section = models.IntegerField()
    article_priority = models.IntegerField()
    linkname = models.CharField(max_length=250)
    linkurl = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'links'


class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    filename_small = models.CharField(max_length=100)
    filename_large = models.CharField(max_length=100)
    filename_original = models.CharField(max_length=100, blank=True)
    photographer_id = models.IntegerField(blank=True, null=True)
    credit = models.CharField(max_length=100)
    caption = models.TextField()
    article_id = models.IntegerField(blank=True, null=True)
    article_date = models.DateField()
    article_section = models.IntegerField(blank=True, null=True)
    article_priority = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField()
    feature = models.CharField(max_length=1)
    coverphoto = models.IntegerField(blank=True, null=True)
    feature_section = models.IntegerField()
    caption_backup = models.TextField()
    active = models.IntegerField(blank=True, null=True)
    thumbnail_only = models.IntegerField()
    afterpar = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'photo'

""" Won't import this """
class Quote(models.Model):
    id = models.AutoField(primary_key=True)
    quote = models.TextField(blank=True)
    attribution = models.CharField(max_length=150, blank=True)
    source = models.CharField(max_length=150, blank=True)
    public = models.IntegerField()
    active = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'quote'

""" Won't import this """
class Related(models.Model):
    id = models.AutoField(primary_key=True)
    article_id = models.IntegerField()
    article_date = models.DateField()
    article_section = models.IntegerField()
    article_priority = models.IntegerField()
    label = models.CharField(max_length=250)
    url = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'related'


class Section(models.Model):
    id = models.AutoField(primary_key=True)
    priority = models.IntegerField()
    name = models.CharField(max_length=100)
    shortname = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'section'


class Series(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    photo = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'series'

""" Won't import this """
class Settings(models.Model):
    name = models.CharField(max_length=255, blank=True)
    int_value = models.IntegerField(blank=True, null=True)
    string_value = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'settings'

""" Won't import this """
class Ted(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'ted'

""" Have been imported """
class Tips(models.Model):
    id = models.AutoField(primary_key=True)
    tip = models.TextField(blank=True)
    submitted = models.DateTimeField()
    user_location = models.CharField(max_length=255, blank=True)
    user_referer = models.CharField(max_length=255, blank=True)
    user_ip = models.CharField(max_length=255, blank=True)
    user_host = models.CharField(max_length=255, blank=True)
    user_agent = models.CharField(max_length=255, blank=True)
    prompt = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'tips'

""" Won't import this """
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'users'

""" Have been imported """
class Volume(models.Model):
    id = models.AutoField(primary_key=True)
    arabic = models.IntegerField()
    roman = models.CharField(max_length=11)
    annodomini = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'volume'