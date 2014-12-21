# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_datum_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='file',
            field=models.FileField(null=True, upload_to='static/uploads', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datum',
            name='datum_type',
            field=models.CharField(max_length=255, choices=[('numeric', 'Numeric'), ('long_text', 'Long Text'), ('short_text', 'Short Text'), ('choice', 'Choice'), ('multi_choice', 'Multi Choice'), ('range', 'Range'), ('image', 'Image')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datum',
            name='max_value',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datum',
            name='min_value',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='response',
            name='choices',
            field=models.ManyToManyField(to='data.Choice', null=True),
            preserve_default=True,
        ),
    ]
