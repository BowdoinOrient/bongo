# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0009_auto_20140414_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip',
            name='submitted_from',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AlterField(
            model_name='tip',
            name='useragent',
            field=models.TextField(null=True),
        ),
    ]
