# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('run_from', models.DateField()),
                ('run_through', models.DateField()),
                ('url', models.URLField(null=True, blank=True)),
                ('adfile', models.ImageField(upload_to='ads')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Advertiser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('run_from', models.DateTimeField()),
                ('run_through', models.DateTimeField()),
                ('message', models.TextField()),
                ('urgent', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('twitter', models.CharField(null=True, max_length=15, blank=True)),
                ('profpic', models.ImageField(null=True, upload_to='headshots', blank=True)),
                ('courtesyof', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HTML',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('content', models.TextField()),
                ('caption', models.TextField(null=True, blank=True)),
                ('creators', models.ManyToManyField(to='bongo.Creator')),
            ],
            options={
                'verbose_name_plural': 'HTML',
                'verbose_name': 'HTML',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('issue_date', models.DateField()),
                ('issue_number', models.IntegerField()),
                ('scribd', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PDF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('staticfile', models.FileField(upload_to='pdfs')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('staticfile', models.ImageField(upload_to='photos')),
                ('caption', models.TextField(null=True, blank=True)),
                ('creators', models.ManyToManyField(to='bongo.Creator')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('published', models.DateTimeField()),
                ('is_published', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=180)),
                ('slug', models.CharField(max_length=180, verbose_name='Slug. WARNING: Changing this will change the post URL, breaking existing links.')),
                ('opinion', models.BooleanField(default=False)),
                ('views_local', models.IntegerField(editable=False, default=0)),
                ('views_global', models.IntegerField(editable=False, default=0)),
                ('primary_type', models.CharField(max_length=8, choices=[('text', 'Article'), ('photo', 'Photo(s)'), ('video', 'Video(s)'), ('liveblog', 'Liveblog'), ('html', 'Interactive/Embedded'), ('generic', 'Other')], default='generic')),
                ('html', models.ManyToManyField(null=True, to='bongo.HTML', blank=True)),
                ('issue', models.ForeignKey(null=True, to='bongo.Issue', blank=True)),
                ('pdf', models.ManyToManyField(null=True, to='bongo.PDF', blank=True)),
                ('photo', models.ManyToManyField(null=True, to='bongo.Photo', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pullquote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
            name='ScheduledPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('section', models.CharField(max_length=8, choices=[('News', 'News'), ('Features', 'Features'), ('A&E', 'Arts & Entertainment'), ('Opinion', 'Opinion'), ('Sports', 'Sports')], default='News')),
                ('priority', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Series',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('tag', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('body', models.TextField()),
                ('excerpt', models.TextField(editable=False, null=True)),
                ('caption', models.TextField(null=True, blank=True)),
                ('creators', models.ManyToManyField(to='bongo.Creator')),
            ],
            options={
                'verbose_name_plural': 'Text',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('content', models.TextField()),
                ('respond_to', models.EmailField(null=True, max_length=75, blank=True)),
                ('submitted_at', models.DateTimeField()),
                ('submitted_from', models.GenericIPAddressField(null=True)),
                ('useragent', models.TextField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('host', models.CharField(max_length=7, choices=[('YouTube', 'YouTube'), ('Vimeo', 'Vimeo'), ('Vine', 'Vine')], default='Vimeo')),
                ('uid', models.CharField(max_length=20, verbose_name='Video identifier - typically a string of letters or numbers after the last slash in the URL')),
                ('caption', models.TextField(null=True, blank=True)),
                ('creators', models.ManyToManyField(to='bongo.Creator')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('volume_number', models.IntegerField()),
                ('volume_year_start', models.IntegerField()),
                ('volume_year_end', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='pullquote',
            field=models.ManyToManyField(null=True, to='bongo.Pullquote', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='section',
            field=models.ForeignKey(to='bongo.Section'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='series',
            field=models.ManyToManyField(null=True, to='bongo.Series', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(null=True, to='bongo.Tag', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.ManyToManyField(null=True, to='bongo.Text', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.ManyToManyField(null=True, to='bongo.Video', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='volume',
            field=models.ForeignKey(to='bongo.Volume'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='issue',
            name='volume',
            field=models.ForeignKey(to='bongo.Volume'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creator',
            name='job',
            field=models.ForeignKey(null=True, to='bongo.Job'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creator',
            name='user',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ad',
            name='owner',
            field=models.ForeignKey(to='bongo.Advertiser'),
            preserve_default=True,
        ),
    ]
