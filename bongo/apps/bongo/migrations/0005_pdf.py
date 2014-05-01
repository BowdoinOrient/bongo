# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'bongo', b'0004_html_issue'),
    ]

    operations = [
        migrations.CreateModel(
            name=b'PDF',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, primary_key=True, to_field='id', serialize=False, to=b'bongo.Content')),
                (b'staticfile', models.FileField(upload_to=b'')),
            ],
            options={
            },
            bases=(b'bongo.content',),
        ),
    ]
