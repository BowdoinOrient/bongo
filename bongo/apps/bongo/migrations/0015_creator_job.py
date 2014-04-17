# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0014_auto_20140417_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='creator',
            name='job',
            field=models.ForeignKey(to='bongo.Job', default=None, to_field=u'id'),
            preserve_default=False,
        ),
    ]
