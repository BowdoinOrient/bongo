# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0013_auto_20140710_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='attribution',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
