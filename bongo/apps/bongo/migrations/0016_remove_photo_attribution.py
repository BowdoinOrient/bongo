# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0015_creator_courtesyof'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='attribution',
        ),
    ]
