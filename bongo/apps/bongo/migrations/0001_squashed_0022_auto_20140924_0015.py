# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [(b'bongo', '0001_initial'), (b'bongo', '0002_creator'), (b'bongo', '0003_content'), (b'bongo', '0004_html_issue'), (b'bongo', '0005_pdf'), (b'bongo', '0006_photo'), (b'bongo', '0007_post'), (b'bongo', '0008_pullquote'), (b'bongo', '0009_text'), (b'bongo', '0010_video'), (b'bongo', '0011_auto_20140502_0025'), (b'bongo', '0012_post_opinion'), (b'bongo', '0013_auto_20140710_2338'), (b'bongo', '0014_photo_attribution'), (b'bongo', '0015_creator_courtesyof'), (b'bongo', '0016_remove_photo_attribution'), (b'bongo', '0017_auto_20140913_1325'), (b'bongo', '0018_auto_20140913_1327'), (b'bongo', '0019_html_pdf_photo_pullquote_text_video'), (b'bongo', '0020_auto_20140913_1630'), (b'bongo', '0021_remove_post_creators'), (b'bongo', '0022_auto_20140924_0015')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name=b'Volume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'volume_number', models.IntegerField()),
                (b'volume_year_start', models.IntegerField()),
                (b'volume_year_end', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name=b'Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name=b'ScheduledPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name=b'Advertiser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name=b'Tip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'content', models.TextField()),
                (b'respond_to', models.EmailField(max_length=75, null=True, blank=True)),
                (b'submitted_at', models.DateTimeField()),
                (b'submitted_from', models.GenericIPAddressField(null=True)),
                (b'useragent', models.TextField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name=b'Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'tag', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name=b'Series',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name=b'Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'section', models.CharField(default=b'News', max_length=8, choices=[(b'News', b'News'), (b'Features', b'Features'), (b'A&E', b'Arts & Entertainment'), (b'Opinion', b'Opinion'), (b'Sports', b'Sports')])),
                (b'priority', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name=b'Alert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'run_from', models.DateTimeField()),
                (b'run_through', models.DateTimeField()),
                (b'message', models.TextField()),
                (b'urgent', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name=b'Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'title', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name=b'Ad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'run_from', models.DateField()),
                (b'run_through', models.DateField()),
                (b'owner', models.ForeignKey(to=b'bongo.Advertiser', to_field='id')),
                (b'url', models.URLField(null=True, blank=True)),
                (b'adfile', models.ImageField(upload_to=b'ads')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name=b'Creator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'user', models.ForeignKey(to_field='id', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                (b'name', models.CharField(max_length=100)),
                (b'job', models.ForeignKey(to=b'bongo.Job', to_field='id')),
                (b'twitter', models.CharField(max_length=15, null=True, blank=True)),
                (b'profpic', models.ImageField(null=True, upload_to=b'', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
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
                (b'slug', models.CharField(max_length=180, verbose_name=b'Slug. WARNING: Changing this will change the post URL, breaking existing links.')),
                (b'views_local', models.IntegerField(default=0, editable=False)),
                (b'views_global', models.IntegerField(default=0, editable=False)),
                (b'primary_type', models.CharField(default=b'generic', max_length=8, choices=[(b'text', b'Article'), (b'photo', b'Photo(s)'), (b'video', b'Video(s)'), (b'liveblog', b'Liveblog'), (b'html', b'Interactive/Embedded'), (b'generic', b'Other')])),
                (b'series', models.ManyToManyField(to=b'bongo.Series', null=True, blank=True)),
                (b'tags', models.ManyToManyField(to=b'bongo.Tag', null=True, blank=True)),
                (b'creators', models.ManyToManyField(to=b'bongo.Creator')),
                ('opinion', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name=b'creator',
            name=b'job',
            field=models.ForeignKey(to=b'bongo.Job', to_field='id', null=True),
        ),
        migrations.AlterField(
            model_name='creator',
            name='profpic',
            field=models.ImageField(null=True, upload_to=b'headshots', blank=True),
        ),
        migrations.AddField(
            model_name='creator',
            name='courtesyof',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterModelOptions(
            name='series',
            options={'verbose_name_plural': 'Series'},
        ),
        migrations.CreateModel(
            name='HTML',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('caption', models.TextField(null=True, blank=True)),
                ('creators', models.ManyToManyField(to=b'bongo.Creator')),
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
                ('creators', models.ManyToManyField(to=b'bongo.Creator')),
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
                ('creators', models.ManyToManyField(to=b'bongo.Creator')),
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
                ('creators', models.ManyToManyField(to=b'bongo.Creator')),
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
                ('creators', models.ManyToManyField(to=b'bongo.Creator')),
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
                ('creators', models.ManyToManyField(to=b'bongo.Creator')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='html',
            field=models.ManyToManyField(to=b'bongo.HTML', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='pdf',
            field=models.ManyToManyField(to=b'bongo.PDF', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ManyToManyField(to=b'bongo.Photo', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='pullquote',
            field=models.ManyToManyField(to=b'bongo.Pullquote', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.ManyToManyField(to=b'bongo.Text', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.ManyToManyField(to=b'bongo.Video', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='post',
            name=b'creators',
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(editable=False),
        ),
    ]
