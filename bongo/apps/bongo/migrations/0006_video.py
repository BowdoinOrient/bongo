# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0005_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('staticfile', models.FileField(upload_to='')),
                ('caption', models.TextField(null=True, blank=True)),
                ('filmers', models.ManyToManyField(to='bongo.Creator')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
