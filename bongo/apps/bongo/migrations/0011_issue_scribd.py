# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0010_auto_20140414_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='scribd',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
