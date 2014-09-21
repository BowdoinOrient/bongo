# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0020_auto_20140913_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='staticfile',
            field=models.FileField(null=True, upload_to=b'pdfs'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='staticfile',
            field=models.ImageField(null=True, upload_to=b'photos'),
        ),
    ]
