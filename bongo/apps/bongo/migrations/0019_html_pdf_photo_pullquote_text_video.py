# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0018_auto_20140913_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='HTML',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('caption', models.TextField(null=True, blank=True)),
                ('creators', models.ManyToManyField(to='bongo.Creator')),
            ],
            options={
                'verbose_name': 'HTML',
                'verbose_name_plural': 'HTML',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PDF',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('staticfile', models.FileField(upload_to=b'pdfs')),
                ('caption', models.TextField(null=True, blank=True)),
                ('creators', models.ManyToManyField(to='bongo.Creator')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('staticfile', models.ImageField(upload_to=b'photos')),
                ('caption', models.TextField(null=True, blank=True)),
                ('creators', models.ManyToManyField(to='bongo.Creator')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pullquote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quote', models.TextField()),
                ('attribution', models.TextField(null=True, blank=True)),
                ('caption', models.TextField(null=True, blank=True)),
                ('creators', models.ManyToManyField(to='bongo.Creator')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField()),
                ('excerpt', models.TextField(null=True, editable=False)),
                ('caption', models.TextField(null=True, blank=True)),
                ('creators', models.ManyToManyField(to='bongo.Creator')),
            ],
            options={
                'verbose_name_plural': 'Text',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host', models.CharField(default=b'Vimeo', max_length=7, choices=[(b'YouTube', b'YouTube'), (b'Vimeo', b'Vimeo'), (b'Vine', b'Vine')])),
                ('uid', models.CharField(max_length=20, verbose_name=b'Video identifier - typically a string of letters or numbers after the last slash in the URL')),
                ('caption', models.TextField(null=True, blank=True)),
                ('creators', models.ManyToManyField(to='bongo.Creator')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
