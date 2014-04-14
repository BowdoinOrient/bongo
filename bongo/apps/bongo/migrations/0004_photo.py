# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bongo', '0003_html_issue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('photographer', models.ForeignKey(to='bongo.Creator', to_field=u'id')),
                ('staticfile', models.FileField(upload_to='')),
                ('caption', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
