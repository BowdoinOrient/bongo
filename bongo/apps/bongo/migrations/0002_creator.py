# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to_field=u'id', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=40, null=True, blank=True)),
                ('twitter', models.CharField(max_length=15, null=True, blank=True)),
                ('profpic', models.FileField(null=True, upload_to='', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
