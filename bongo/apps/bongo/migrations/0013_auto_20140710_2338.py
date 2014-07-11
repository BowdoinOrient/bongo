# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0012_post_opinion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='adfile',
            field=models.ImageField(upload_to=b'ads'),
        ),
        migrations.AlterField(
            model_name='creator',
            name='profpic',
            field=models.ImageField(null=True, upload_to=b'headshots', blank=True),
        ),
        migrations.AlterField(
            model_name='pdf',
            name='staticfile',
            field=models.FileField(upload_to=b'pdfs'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='staticfile',
            field=models.ImageField(upload_to=b'photos'),
        ),
        migrations.AlterField(
            model_name='pullquote',
            name='attribution',
            field=models.TextField(null=True, blank=True),
        ),
    ]
