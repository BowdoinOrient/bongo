# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0015_creator_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='priority',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='section',
            name='section',
            field=models.CharField(default='News', max_length=8, choices=[('News', 'News'), ('Features', 'Features'), ('A&E', 'Arts & Entertainment'), ('Opinion', 'Opinion'), ('Sports', 'Sports')]),
        ),
    ]
