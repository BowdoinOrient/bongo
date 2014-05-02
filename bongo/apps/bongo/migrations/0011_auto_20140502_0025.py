# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'bongo', b'0010_video'),
    ]

    operations = [
        migrations.AddField(
            model_name=b'post',
            name=b'content',
            field=models.ManyToManyField(to=b'bongo.Content', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name=b'post',
            name=b'slug',
            field=models.CharField(max_length=180, verbose_name=b'Slug. WARNING: Changing this will change the post URL, breaking existing links.'),
        ),
        migrations.AlterField(
            model_name=b'creator',
            name=b'job',
            field=models.ForeignKey(to=b'bongo.Job', to_field='id', null=True),
        ),
    ]
