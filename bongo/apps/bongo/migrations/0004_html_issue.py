# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'bongo', b'0003_content'),
    ]

    operations = [
        migrations.CreateModel(
            name=b'HTML',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, primary_key=True, to_field='id', serialize=False, to=b'bongo.Content')),
                (b'content', models.TextField()),
            ],
            options={
            },
            bases=(b'bongo.content',),
        ),
        migrations.CreateModel(
            name=b'Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'issue_date', models.DateField()),
                (b'issue_number', models.IntegerField()),
                (b'volume', models.ForeignKey(to=b'bongo.Volume', to_field='id')),
                (b'scribd', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
