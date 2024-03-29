# Generated by Django 3.2.15 on 2024-03-29 19:27

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inforecords', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatasetType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('slug', models.CharField(max_length=20, unique=True)),
                ('has_multiple_datasets', models.BooleanField(default=False)),
                ('x_axis_title', models.CharField(max_length=40)),
                ('y_axis_title', models.CharField(max_length=40)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Dataset type',
                'verbose_name_plural': 'Dataset types',
            },
        ),
        migrations.CreateModel(
            name='GeneratorState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_last_run', models.DateTimeField()),
                ('check_is_running', models.BooleanField(default=False)),
                ('update_last_run', models.DateTimeField()),
                ('update_is_running', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='HistogramType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('slug', models.CharField(max_length=20, unique=True)),
                ('has_multiple_datasets', models.BooleanField(default=False)),
                ('bin_axis_title', models.CharField(max_length=40)),
                ('value_axis_title', models.CharField(max_length=40)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Histogram type',
                'verbose_name_plural': 'Histogram types',
            },
        ),
        migrations.CreateModel(
            name='NetworkSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('num_coincidences', models.IntegerField(blank=True, null=True)),
                ('needs_update', models.BooleanField(default=False)),
                ('needs_update_coincidences', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Network summary',
                'verbose_name_plural': 'Network summaries',
                'ordering': ['date'],
                'get_latest_by': 'date',
            },
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('num_events', models.IntegerField(blank=True, null=True)),
                ('num_config', models.IntegerField(blank=True, null=True)),
                ('num_errors', models.IntegerField(blank=True, null=True)),
                ('num_weather', models.IntegerField(blank=True, null=True)),
                ('num_singles', models.IntegerField(blank=True, null=True)),
                ('needs_update', models.BooleanField(default=False)),
                ('needs_update_events', models.BooleanField(default=False)),
                ('needs_update_config', models.BooleanField(default=False)),
                ('needs_update_errors', models.BooleanField(default=False)),
                ('needs_update_weather', models.BooleanField(default=False)),
                ('needs_update_singles', models.BooleanField(default=False)),
                ('events_in_last_hour', models.BooleanField(default=False)),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='summaries', to='inforecords.station')),
            ],
            options={
                'verbose_name': 'Summary',
                'verbose_name_plural': 'Summaries',
                'ordering': ['date', 'station'],
                'get_latest_by': 'date',
                'unique_together': {('station', 'date')},
            },
        ),
        migrations.CreateModel(
            name='DetectorTimingOffset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offset_1', models.FloatField(blank=True, null=True)),
                ('offset_2', models.FloatField(blank=True, null=True)),
                ('offset_3', models.FloatField(blank=True, null=True)),
                ('offset_4', models.FloatField(blank=True, null=True)),
                ('summary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detector_timing_offsets', to='histograms.summary')),
            ],
            options={
                'verbose_name': 'Detector timing offset',
                'verbose_name_plural': 'Detector timing offsets',
                'ordering': ['summary'],
            },
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('gps_latitude', models.FloatField()),
                ('gps_longitude', models.FloatField()),
                ('gps_altitude', models.FloatField()),
                ('mas_version', models.CharField(max_length=40)),
                ('slv_version', models.CharField(max_length=40)),
                ('trig_low_signals', models.PositiveIntegerField()),
                ('trig_high_signals', models.PositiveIntegerField()),
                ('trig_external', models.PositiveIntegerField()),
                ('trig_and_or', models.BooleanField()),
                ('precoinctime', models.FloatField()),
                ('coinctime', models.FloatField()),
                ('postcoinctime', models.FloatField()),
                ('detnum', models.PositiveIntegerField()),
                ('spare_bytes', models.PositiveSmallIntegerField()),
                ('use_filter', models.BooleanField()),
                ('use_filter_threshold', models.BooleanField()),
                ('reduce_data', models.BooleanField()),
                ('startmode', models.BooleanField()),
                ('delay_screen', models.FloatField()),
                ('delay_check', models.FloatField()),
                ('delay_error', models.FloatField()),
                ('mas_ch1_thres_low', models.FloatField()),
                ('mas_ch1_thres_high', models.FloatField()),
                ('mas_ch2_thres_low', models.FloatField()),
                ('mas_ch2_thres_high', models.FloatField()),
                ('mas_ch1_inttime', models.FloatField()),
                ('mas_ch2_inttime', models.FloatField()),
                ('mas_ch1_voltage', models.FloatField()),
                ('mas_ch2_voltage', models.FloatField()),
                ('mas_ch1_current', models.FloatField()),
                ('mas_ch2_current', models.FloatField()),
                ('mas_comp_thres_low', models.FloatField()),
                ('mas_comp_thres_high', models.FloatField()),
                ('mas_max_voltage', models.FloatField()),
                ('mas_reset', models.BooleanField()),
                ('mas_ch1_gain_pos', models.PositiveSmallIntegerField()),
                ('mas_ch1_gain_neg', models.PositiveSmallIntegerField()),
                ('mas_ch2_gain_pos', models.PositiveSmallIntegerField()),
                ('mas_ch2_gain_neg', models.PositiveSmallIntegerField()),
                ('mas_ch1_offset_pos', models.PositiveSmallIntegerField()),
                ('mas_ch1_offset_neg', models.PositiveSmallIntegerField()),
                ('mas_ch2_offset_pos', models.PositiveSmallIntegerField()),
                ('mas_ch2_offset_neg', models.PositiveSmallIntegerField()),
                ('mas_common_offset', models.PositiveSmallIntegerField()),
                ('mas_internal_voltage', models.PositiveSmallIntegerField()),
                ('mas_ch1_adc_gain', models.FloatField()),
                ('mas_ch1_adc_offset', models.FloatField()),
                ('mas_ch2_adc_gain', models.FloatField()),
                ('mas_ch2_adc_offset', models.FloatField()),
                ('mas_ch1_comp_gain', models.FloatField()),
                ('mas_ch1_comp_offset', models.FloatField()),
                ('mas_ch2_comp_gain', models.FloatField()),
                ('mas_ch2_comp_offset', models.FloatField()),
                ('slv_ch1_thres_low', models.FloatField()),
                ('slv_ch1_thres_high', models.FloatField()),
                ('slv_ch2_thres_low', models.FloatField()),
                ('slv_ch2_thres_high', models.FloatField()),
                ('slv_ch1_inttime', models.FloatField()),
                ('slv_ch2_inttime', models.FloatField()),
                ('slv_ch1_voltage', models.FloatField()),
                ('slv_ch2_voltage', models.FloatField()),
                ('slv_ch1_current', models.FloatField()),
                ('slv_ch2_current', models.FloatField()),
                ('slv_comp_thres_low', models.FloatField()),
                ('slv_comp_thres_high', models.FloatField()),
                ('slv_max_voltage', models.FloatField()),
                ('slv_reset', models.BooleanField()),
                ('slv_ch1_gain_pos', models.PositiveSmallIntegerField()),
                ('slv_ch1_gain_neg', models.PositiveSmallIntegerField()),
                ('slv_ch2_gain_pos', models.PositiveSmallIntegerField()),
                ('slv_ch2_gain_neg', models.PositiveSmallIntegerField()),
                ('slv_ch1_offset_pos', models.PositiveSmallIntegerField()),
                ('slv_ch1_offset_neg', models.PositiveSmallIntegerField()),
                ('slv_ch2_offset_pos', models.PositiveSmallIntegerField()),
                ('slv_ch2_offset_neg', models.PositiveSmallIntegerField()),
                ('slv_common_offset', models.PositiveSmallIntegerField()),
                ('slv_internal_voltage', models.PositiveSmallIntegerField()),
                ('slv_ch1_adc_gain', models.FloatField()),
                ('slv_ch1_adc_offset', models.FloatField()),
                ('slv_ch2_adc_gain', models.FloatField()),
                ('slv_ch2_adc_offset', models.FloatField()),
                ('slv_ch1_comp_gain', models.FloatField()),
                ('slv_ch1_comp_offset', models.FloatField()),
                ('slv_ch2_comp_gain', models.FloatField()),
                ('slv_ch2_comp_offset', models.FloatField()),
                ('summary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='configurations', to='histograms.summary')),
            ],
            options={
                'verbose_name': 'Configuration',
                'verbose_name_plural': 'Configurations',
                'ordering': ['summary'],
                'get_latest_by': 'timestamp',
            },
        ),
        migrations.CreateModel(
            name='StationTimingOffset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offset', models.FloatField(blank=True, null=True)),
                ('error', models.FloatField(blank=True, null=True)),
                ('ref_summary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ref_station_offsets', to='histograms.summary')),
                ('summary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='station_offsets', to='histograms.summary')),
            ],
            options={
                'verbose_name': 'Station timing offset',
                'verbose_name_plural': 'Station timing offsets',
                'ordering': ['ref_summary'],
                'unique_together': {('ref_summary', 'summary')},
            },
        ),
        migrations.CreateModel(
            name='NetworkHistogram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bins', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), size=None)),
                ('values', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), size=None)),
                ('network_summary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='network_histograms', to='histograms.networksummary')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='network_histograms', to='histograms.histogramtype')),
            ],
            options={
                'verbose_name': 'Network histogram',
                'verbose_name_plural': 'Network histograms',
                'ordering': ['network_summary', 'type'],
                'unique_together': {('network_summary', 'type')},
            },
        ),
        migrations.CreateModel(
            name='MultiDailyHistogram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bins', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), size=None)),
                ('values', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), size=None), size=4)),
                ('summary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multi_histograms', to='histograms.summary')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multi_histograms', to='histograms.histogramtype')),
            ],
            options={
                'ordering': ['summary', 'type'],
                'abstract': False,
                'unique_together': {('summary', 'type')},
            },
        ),
        migrations.CreateModel(
            name='MultiDailyDataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), size=None)),
                ('y', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None), size=4)),
                ('summary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multi_datasets', to='histograms.summary')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multi_datasets', to='histograms.datasettype')),
            ],
            options={
                'ordering': ['summary', 'type'],
                'abstract': False,
                'unique_together': {('summary', 'type')},
            },
        ),
        migrations.CreateModel(
            name='DailyHistogram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bins', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), size=None)),
                ('values', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), size=None)),
                ('summary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='histograms', to='histograms.summary')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='histograms', to='histograms.histogramtype')),
            ],
            options={
                'ordering': ['summary', 'type'],
                'abstract': False,
                'unique_together': {('summary', 'type')},
            },
        ),
        migrations.CreateModel(
            name='DailyDataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), size=None)),
                ('y', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None)),
                ('summary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datasets', to='histograms.summary')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datasets', to='histograms.datasettype')),
            ],
            options={
                'ordering': ['summary', 'type'],
                'abstract': False,
                'unique_together': {('summary', 'type')},
            },
        ),
    ]
