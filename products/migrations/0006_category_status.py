# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20161103_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]
