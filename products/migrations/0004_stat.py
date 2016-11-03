# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20161102_1852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Category_count', models.IntegerField()),
            ],
        ),
    ]
