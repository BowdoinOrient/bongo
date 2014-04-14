# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0004_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField()),
                ('authors', models.ManyToManyField(to='bongo.Creator')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
