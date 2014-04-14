# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0007_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('primary_type', models.CharField(default='news', max_length=8, choices=[('news', 'News'), ('features', 'Features'), ('ae', 'Arts & Entertainment'), ('opinion', 'Opinion'), ('sports', 'Sports')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tips',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('respond_to', models.EmailField(max_length=75, null=True, blank=True)),
                ('submitted_at', models.DateTimeField()),
                ('submitted_from', models.GenericIPAddressField()),
                ('useragent', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='views_local',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='views_global',
            field=models.IntegerField(default=0, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', max_length=180, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='bongo.Tag', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='section',
            field=models.ForeignKey(to='bongo.Section', default=None, to_field=u'id'),
            preserve_default=False,
        ),
    ]
