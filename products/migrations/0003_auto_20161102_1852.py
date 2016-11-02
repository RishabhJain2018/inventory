# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20161002_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Stat',
        ),
        migrations.RemoveField(
            model_name='category',
            name='status',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
