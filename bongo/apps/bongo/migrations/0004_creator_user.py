# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '__first__'),
        (b'bongo', b'0003_post'),
    ]

    operations = [
        migrations.AddField(
            model_name=b'creator',
            name=b'user',
            field=models.ForeignKey(to_field='id', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
