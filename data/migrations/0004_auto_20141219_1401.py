# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20141219_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datum',
            name='datum_type',
            field=models.CharField(max_length=255, choices=[('numeric', 'Numeric'), ('long_text', 'Long Text'), ('short_text', 'Short Text'), ('choice', 'Choice'), ('multi_choice', 'Multi Choice'), ('scale', 'Scale')]),
            preserve_default=True,
        ),
    ]
