# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0008_auto_20140414_1705'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tips',
            new_name='Tip',
        ),
        migrations.AddField(
            model_name='text',
            name='excerpt',
            field=models.TextField(null=True, editable=False),
            preserve_default=True,
        ),
        migrations.RenameField(
            model_name='section',
            old_name='primary_type',
            new_name='section',
        ),
    ]
