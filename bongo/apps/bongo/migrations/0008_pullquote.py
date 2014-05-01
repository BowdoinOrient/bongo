# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'bongo', b'0007_post'),
    ]

    operations = [
        migrations.CreateModel(
            name=b'Pullquote',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, primary_key=True, to_field='id', serialize=False, to=b'bongo.Content')),
                (b'quote', models.TextField()),
                (b'attribution', models.TextField()),
            ],
            options={
            },
            bases=(b'bongo.content',),
        ),
    ]
