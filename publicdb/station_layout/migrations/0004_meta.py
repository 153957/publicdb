# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-06 11:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('station_layout', '0003_increase_emailfield_length'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stationlayout',
            options={'get_latest_by': 'active_date', 'ordering': ['station', 'active_date'], 'verbose_name': 'Station layout', 'verbose_name_plural': 'Station layouts'},
        ),
        migrations.AlterModelOptions(
            name='stationlayoutquarantine',
            options={'verbose_name': 'Station layout quarantine', 'verbose_name_plural': 'Station layouts quarantine'},
        ),
    ]