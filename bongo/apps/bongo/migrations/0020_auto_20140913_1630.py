# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0019_html_pdf_photo_pullquote_text_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='html',
            field=models.ManyToManyField(to='bongo.HTML', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='pdf',
            field=models.ManyToManyField(to='bongo.PDF', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ManyToManyField(to='bongo.Photo', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='pullquote',
            field=models.ManyToManyField(to='bongo.Pullquote', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.ManyToManyField(to='bongo.Text', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.ManyToManyField(to='bongo.Video', null=True, blank=True),
            preserve_default=True,
        ),
    ]
