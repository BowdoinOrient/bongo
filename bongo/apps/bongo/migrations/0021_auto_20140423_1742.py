# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0020_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='creators',
            field=models.ManyToManyField(default=None, to='bongo.Creator'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='content',
            name='caption',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='post',
            name='html',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='caption',
        ),
        migrations.RemoveField(
            model_name='post',
            name='pdf',
        ),
        migrations.RemoveField(
            model_name='pdf',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='photographer',
        ),
        migrations.RemoveField(
            model_name='video',
            name='filmers',
        ),
        migrations.RemoveField(
            model_name='post',
            name='photos',
        ),
        migrations.RemoveField(
            model_name='html',
            name='designers',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.RemoveField(
            model_name='text',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='video',
            name='caption',
        ),
        migrations.RemoveField(
            model_name='html',
            name='caption',
        ),
        migrations.RemoveField(
            model_name='post',
            name='video',
        ),
        migrations.RemoveField(
            model_name='pdf',
            name='caption',
        ),
    ]
