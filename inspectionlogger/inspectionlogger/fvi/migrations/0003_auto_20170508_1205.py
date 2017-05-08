# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-08 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fvi', '0002_auto_20170419_1439'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inspection',
            options={'permissions': (('create_inspection', 'can create inspetions'), ('view_inspection', 'can view inspections'), ('update_inspection', 'cann update inspections'))},
        ),
        migrations.AlterField(
            model_name='inspectionitemstatus',
            name='complianceStatus',
            field=models.IntegerField(choices=[(0, 'not in compliance'), (1, 'in compliance'), (2, 'not observed'), (3, 'not applicable '), (5, 'corrected on site')]),
        ),
    ]
