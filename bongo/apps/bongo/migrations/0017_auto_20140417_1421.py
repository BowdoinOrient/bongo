# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0016_auto_20140417_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='adfile',
            field=models.ImageField(default=None, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='creator',
            name='profpic',
            field=models.ImageField(null=True, upload_to='', blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='staticfile',
            field=models.ImageField(upload_to=''),
        ),
    ]
