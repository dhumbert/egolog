# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_response'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='response',
            unique_together=set([('user', 'date', 'prompt')]),
        ),
    ]
