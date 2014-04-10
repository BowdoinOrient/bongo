from django.db import models
from django.contrib.auth.models import User

class Article (models.Model):
    pass

class Photo (models.Model):
    pass

class Video (models.Model):
    pass

class Serie (models.Model):
    pass

class Alert (models.Model):
    pass

class Ad (models.Model):
    pass

class Issue(models.Model):
    pass

class Author (models.Model): # Extends to photographers as well, you can be both 
    # possibility this author is also a bongo user
    user = models.ForeignKey(User, null=True)

    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)

    written_works = models.ManyToManyField(Article, null=True)
    photo_works = models.ManyToManyField(Photo, null=True)
    video_works = models.ManyToManyField(Video, null=True)

