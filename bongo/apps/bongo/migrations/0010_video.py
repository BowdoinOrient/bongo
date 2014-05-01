# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'bongo', b'0009_text'),
    ]

    operations = [
        migrations.CreateModel(
            name=b'Video',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, primary_key=True, to_field='id', serialize=False, to=b'bongo.Content')),
                (b'host', models.CharField(default=b'Vimeo', max_length=7, choices=[(b'YouTube', b'YouTube'), (b'Vimeo', b'Vimeo'), (b'Vine', b'Vine')])),
                (b'uid', models.CharField(max_length=20, verbose_name=b'Video identifier - typically a string of letters or numbers after the last slash in the URL')),
            ],
            options={
            },
            bases=(b'bongo.content',),
        ),
    ]
