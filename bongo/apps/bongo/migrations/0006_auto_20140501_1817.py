# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'bongo', b'0005_auto_20140430_1833'),
    ]

    operations = [
        migrations.RenameField(
            model_name=b'pullquote',
            old_name=b'attibution',
            new_name=b'attribution',
        ),
    ]
