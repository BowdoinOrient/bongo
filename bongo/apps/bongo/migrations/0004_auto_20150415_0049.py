# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0003_auto_20141226_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip',
            name='respond_to',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
    ]
