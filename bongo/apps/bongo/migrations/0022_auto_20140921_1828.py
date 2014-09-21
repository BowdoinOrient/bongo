# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0021_auto_20140921_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='volume',
            field=models.ForeignKey(to='bongo.Volume', null=True),
        ),
        migrations.AlterField(
            model_name='pdf',
            name='staticfile',
            field=models.FileField(null=True, upload_to=b'pdfs', blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='staticfile',
            field=models.ImageField(null=True, upload_to=b'photos', blank=True),
        ),
    ]
