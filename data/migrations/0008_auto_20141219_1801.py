# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_auto_20141219_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='datum',
            name='max_value',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='datum',
            name='min_value',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
