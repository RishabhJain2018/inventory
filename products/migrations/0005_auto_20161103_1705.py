# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_stat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stat',
            old_name='Category_count',
            new_name='category_count',
        ),
    ]
