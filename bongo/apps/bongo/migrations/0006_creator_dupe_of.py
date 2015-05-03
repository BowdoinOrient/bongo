# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0005_auto_20150415_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='creator',
            name='dupe_of',
            field=models.ForeignKey(null=True, editable=False, to='bongo.Creator'),
        ),
    ]
