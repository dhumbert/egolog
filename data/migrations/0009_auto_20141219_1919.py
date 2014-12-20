# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_auto_20141219_1801'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='response',
            unique_together=set([('user', 'date')]),
        ),
        migrations.RemoveField(
            model_name='response',
            name='prompt',
        ),
        migrations.AddField(
            model_name='response',
            name='choices',
            field=models.ManyToManyField(to='data.Choice'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='response',
            name='datum',
            field=models.ForeignKey(default=None, to='data.Datum'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='datum',
            name='datum_type',
            field=models.CharField(max_length=255, choices=[('numeric', 'Numeric'), ('long_text', 'Long Text'), ('short_text', 'Short Text'), ('choice', 'Choice'), ('multi_choice', 'Multi Choice'), ('range', 'Range')]),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='response',
            unique_together=set([('user', 'date', 'datum')]),
        ),
    ]
