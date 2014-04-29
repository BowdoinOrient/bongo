# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'bongo', b'0002_content_issue'),
    ]

    operations = [
        migrations.CreateModel(
            name=b'Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'created', models.DateTimeField(auto_now_add=True)),
                (b'updated', models.DateTimeField(auto_now=True)),
                (b'published', models.DateTimeField()),
                (b'is_published', models.BooleanField(default=False)),
                (b'issue', models.ForeignKey(to_field='id', blank=True, to=b'bongo.Issue', null=True)),
                (b'volume', models.ForeignKey(to=b'bongo.Volume', to_field='id')),
                (b'section', models.ForeignKey(to=b'bongo.Section', to_field='id')),
                (b'title', models.CharField(max_length=180)),
                (b'slug', models.CharField(default=b'', max_length=180, editable=False)),
                (b'views_local', models.IntegerField(default=0, editable=False)),
                (b'views_global', models.IntegerField(default=0, editable=False)),
                (b'primary_type', models.CharField(default=b'generic', max_length=8, choices=[(b'text', b'Article'), (b'photo', b'Photo(s)'), (b'video', b'Video(s)'), (b'liveblog', b'Liveblog'), (b'html', b'Interactive/Embedded'), (b'generic', b'Other')])),
                (b'series', models.ManyToManyField(to=b'bongo.Series', null=True, blank=True)),
                (b'tags', models.ManyToManyField(to=b'bongo.Tag', null=True, blank=True)),
                (b'creators', models.ManyToManyField(to=b'bongo.Creator')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
