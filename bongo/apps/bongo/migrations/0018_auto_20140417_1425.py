# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0017_auto_20140417_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDF',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('staticfile', models.FileField(upload_to='')),
                ('caption', models.TextField(null=True, blank=True)),
                ('authors', models.ManyToManyField(to='bongo.Creator')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='pdf',
            field=models.ManyToManyField(to='bongo.PDF', null=True, blank=True),
            preserve_default=True,
        ),
    ]
