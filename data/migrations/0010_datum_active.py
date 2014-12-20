# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_auto_20141219_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='datum',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
