# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='scribd_image',
            field=models.URLField(null=True, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
