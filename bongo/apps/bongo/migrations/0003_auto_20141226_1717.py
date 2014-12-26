# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0002_issue_scribd_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='imported',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='advertiser',
            name='imported',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='alert',
            name='imported',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creator',
            name='imported',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='imported',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='html',
            name='imported',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='issue',
            name='imported',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='imported',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pdf',
            name='imported',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='imported',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='imported',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pullquote',
            name='imported',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scheduledpost',
            name='imported',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='section',
            name='imported',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='series',
            name='imported',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tag',
            name='imported',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='text',
            name='imported',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tip',
            name='imported',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='video',
            name='imported',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='volume',
            name='imported',
            field=models.BooleanField(default=False, editable=False),
            preserve_default=True,
        ),
    ]
