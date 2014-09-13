# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0017_auto_20140913_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name=b'content',
            name=b'creators',
        ),
        migrations.DeleteModel(
            name='Content',
        ),
    ]
