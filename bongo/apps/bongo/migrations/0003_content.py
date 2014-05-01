# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'bongo', b'0002_creator'),
    ]

    operations = [
        migrations.CreateModel(
            name=b'Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'caption', models.TextField(null=True, blank=True)),
                (b'creators', models.ManyToManyField(to=b'bongo.Creator')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
