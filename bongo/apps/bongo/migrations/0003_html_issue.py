# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0002_creator'),
    ]

    operations = [
        migrations.CreateModel(
            name='HTML',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('caption', models.TextField(null=True, blank=True)),
                ('designers', models.ManyToManyField(to='bongo.Creator')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('issue_date', models.DateField()),
                ('issue_number', models.IntegerField()),
                ('volume', models.ForeignKey(to='bongo.Volume', to_field=u'id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
