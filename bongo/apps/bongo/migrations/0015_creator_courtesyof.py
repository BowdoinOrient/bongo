# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0014_photo_attribution'),
    ]

    operations = [
        migrations.AddField(
            model_name='creator',
            name='courtesyof',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
