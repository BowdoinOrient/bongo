# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0016_remove_photo_attribution'),
    ]

    operations = [
        migrations.RemoveField(
            model_name=b'html',
            name='content_ptr',
        ),
        migrations.RemoveField(
            model_name=b'pdf',
            name='content_ptr',
        ),
        migrations.RemoveField(
            model_name=b'photo',
            name='content_ptr',
        ),
        migrations.RemoveField(
            model_name=b'pullquote',
            name='content_ptr',
        ),
        migrations.RemoveField(
            model_name=b'text',
            name='content_ptr',
        ),
        migrations.RemoveField(
            model_name=b'video',
            name='content_ptr',
        ),
        migrations.AlterModelOptions(
            name='content',
            options={'verbose_name_plural': 'Content'},
        ),
        migrations.AlterModelOptions(
            name='series',
            options={'verbose_name_plural': 'Series'},
        ),
        migrations.RemoveField(
            model_name='post',
            name=b'content',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
        migrations.DeleteModel(
            name='Text',
        ),
        migrations.DeleteModel(
            name='Pullquote',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.DeleteModel(
            name='PDF',
        ),
        migrations.DeleteModel(
            name='HTML',
        ),
    ]
