# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0006_auto_20150913_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(db_index=True, max_length=180, verbose_name='Slug. WARNING: Changing this will change the post URL, breaking existing links.'),
        ),
    ]
