# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0004_auto_20150415_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='html',
            field=models.ManyToManyField(blank=True, to='bongo.HTML'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pdf',
            field=models.ManyToManyField(blank=True, to='bongo.PDF'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ManyToManyField(blank=True, to='bongo.Photo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pullquote',
            field=models.ManyToManyField(blank=True, to='bongo.Pullquote'),
        ),
        migrations.AlterField(
            model_name='post',
            name='series',
            field=models.ManyToManyField(blank=True, to='bongo.Series'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='bongo.Tag'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.ManyToManyField(blank=True, to='bongo.Text'),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.ManyToManyField(blank=True, to='bongo.Video'),
        ),
    ]
