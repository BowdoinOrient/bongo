# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0011_auto_20140502_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='opinion',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
