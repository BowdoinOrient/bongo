# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0012_auto_20140417_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='scribd',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
