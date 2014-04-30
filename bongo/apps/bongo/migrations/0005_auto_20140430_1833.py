# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'bongo', b'0004_creator_user'),
    ]

    operations = [
        migrations.AddField(
            model_name=b'video',
            name=b'uid',
            field=models.CharField(default=None, max_length=20, verbose_name=b'Video identifier - typically a string of letters or numbers after the last slash in the URL'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name=b'video',
            name=b'host',
            field=models.CharField(default=b'Vimeo', max_length=7, choices=[(b'YouTube', b'YouTube'), (b'Vimeo', b'Vimeo'), (b'Vine', b'Vine')]),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name=b'video',
            name=b'staticfile',
        ),
    ]
