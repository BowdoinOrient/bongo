# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0006_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('published', models.DateTimeField()),
                ('is_published', models.BooleanField(default=False)),
                ('issue', models.ForeignKey(to_field=u'id', blank=True, to='bongo.Issue', null=True)),
                ('volume', models.ForeignKey(to='bongo.Volume', to_field=u'id')),
                ('title', models.CharField(max_length=180)),
                ('primary_type', models.CharField(default='generic', max_length=8, choices=[('text', 'Article'), ('photo', 'Photo(s)'), ('video', 'Video(s)'), ('liveblog', 'Liveblog'), ('html', 'Interactive/Embedded'), ('generic', 'Other')])),
                ('series', models.ManyToManyField(to='bongo.Series', null=True, blank=True)),
                ('creators', models.ManyToManyField(to='bongo.Creator')),
                ('text', models.ManyToManyField(to='bongo.Text', null=True, blank=True)),
                ('photos', models.ManyToManyField(to='bongo.Photo', null=True, blank=True)),
                ('video', models.ManyToManyField(to='bongo.Video', null=True, blank=True)),
                ('html', models.ManyToManyField(to='bongo.HTML', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
