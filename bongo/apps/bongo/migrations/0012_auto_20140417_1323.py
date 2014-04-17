# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0011_issue_scribd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='run_from',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='alert',
            name='run_through',
            field=models.DateTimeField(),
        ),
    ]
