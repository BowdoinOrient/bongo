# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0020_auto_20140913_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name=b'creators',
        ),
    ]
