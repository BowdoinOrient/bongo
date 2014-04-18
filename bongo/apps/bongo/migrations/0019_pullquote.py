# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0018_auto_20140417_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pullquote',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('quote', models.TextField()),
                ('attibution', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
