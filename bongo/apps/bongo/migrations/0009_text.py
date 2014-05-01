# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'bongo', b'0008_pullquote'),
    ]

    operations = [
        migrations.CreateModel(
            name=b'Text',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, primary_key=True, to_field='id', serialize=False, to=b'bongo.Content')),
                (b'body', models.TextField()),
                (b'excerpt', models.TextField(null=True, editable=False)),
            ],
            options={
            },
            bases=(b'bongo.content',),
        ),
    ]
