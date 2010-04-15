from django.db import models

import zlib
import cPickle as pickle
import base64

from django_publicdb.inforecords import models as inforecords


class SerializedDataField(models.Field):
    # This makes sure that to_python() will be called when objects are
    # initialized
    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        super(SerializedDataField, self).__init__(*args, **kwargs)

    def db_type(self):
        return 'LONGBLOB'

    def to_python(self, value):
        try:
            unpickled = pickle.loads(zlib.decompress(base64.b64decode(value)))
        except:
            return value
        else:
            return unpickled

    def get_db_prep_value(self, value):
        return base64.b64encode(zlib.compress(pickle.dumps(value)))

class Summary(models.Model):
    station = models.ForeignKey(inforecords.Station)
    date = models.DateField()
    num_events = models.IntegerField(blank=True, null=True)
    num_config = models.IntegerField(blank=True, null=True)
    num_errors = models.IntegerField(blank=True, null=True)
    num_weather = models.IntegerField(blank=True, null=True)
    needs_update = models.BooleanField()
    needs_update_events = models.BooleanField()
    needs_update_config = models.BooleanField()
    needs_update_errors = models.BooleanField()
    needs_update_weather = models.BooleanField()

    def __unicode__(self):
        return 'Summary: %d - %s' % (self.station.number,
                                     self.date.strftime('%d %b %Y'))

    class Meta:
        verbose_name_plural = 'summaries'
        unique_together = (('station', 'date'),)
        ordering = ('date', 'station')

class Configuration(models.Model):
    source = models.ForeignKey('Summary')
    timestamp = models.DateTimeField()
    gps_latitude = models.FloatField()
    gps_longitude = models.FloatField()
    gps_altitude = models.FloatField()
    mas_version = models.CharField(max_length=40)
    slv_version = models.CharField(max_length=40)
    trig_low_signals = models.PositiveIntegerField()
    trig_high_signals = models.PositiveIntegerField()
    trig_external = models.PositiveIntegerField()
    trig_and_or = models.BooleanField()
    precoinctime = models.FloatField()
    coinctime = models.FloatField()
    postcoinctime = models.FloatField()
    detnum = models.PositiveIntegerField()
    spare_bytes = models.PositiveSmallIntegerField()
    use_filter = models.BooleanField()
    use_filter_threshold = models.BooleanField()
    reduce_data = models.BooleanField()
    startmode = models.BooleanField()
    delay_screen = models.FloatField()
    delay_check = models.FloatField()
    delay_error = models.FloatField()
    mas_ch1_thres_low = models.FloatField()
    mas_ch1_thres_high = models.FloatField()
    mas_ch2_thres_low = models.FloatField()
    mas_ch2_thres_high = models.FloatField()
    mas_ch1_inttime = models.FloatField()
    mas_ch2_inttime = models.FloatField()
    mas_ch1_voltage = models.FloatField()
    mas_ch2_voltage = models.FloatField()
    mas_ch1_current = models.FloatField()
    mas_ch2_current = models.FloatField()
    mas_comp_thres_low = models.FloatField()
    mas_comp_thres_high = models.FloatField()
    mas_max_voltage = models.FloatField()
    mas_reset = models.BooleanField()
    mas_ch1_gain_pos = models.PositiveSmallIntegerField()
    mas_ch1_gain_neg = models.PositiveSmallIntegerField()
    mas_ch2_gain_pos = models.PositiveSmallIntegerField()
    mas_ch2_gain_neg = models.PositiveSmallIntegerField()
    mas_ch1_offset_pos = models.PositiveSmallIntegerField()
    mas_ch1_offset_neg = models.PositiveSmallIntegerField()
    mas_ch2_offset_pos = models.PositiveSmallIntegerField()
    mas_ch2_offset_neg = models.PositiveSmallIntegerField()
    mas_common_offset = models.PositiveSmallIntegerField()
    mas_internal_voltage = models.PositiveSmallIntegerField()
    mas_ch1_adc_gain = models.FloatField()
    mas_ch1_adc_offset = models.FloatField()
    mas_ch2_adc_gain = models.FloatField()
    mas_ch2_adc_offset = models.FloatField()
    mas_ch1_comp_gain = models.FloatField()
    mas_ch1_comp_offset = models.FloatField()
    mas_ch2_comp_gain = models.FloatField()
    mas_ch2_comp_offset = models.FloatField()
    slv_ch1_thres_low = models.FloatField()
    slv_ch1_thres_high = models.FloatField()
    slv_ch2_thres_low = models.FloatField()
    slv_ch2_thres_high = models.FloatField()
    slv_ch1_inttime = models.FloatField()
    slv_ch2_inttime = models.FloatField()
    slv_ch1_voltage = models.FloatField()
    slv_ch2_voltage = models.FloatField()
    slv_ch1_current = models.FloatField()
    slv_ch2_current = models.FloatField()
    slv_comp_thres_low = models.FloatField()
    slv_comp_thres_high = models.FloatField()
    slv_max_voltage = models.FloatField()
    slv_reset = models.BooleanField()
    slv_ch1_gain_pos = models.PositiveSmallIntegerField()
    slv_ch1_gain_neg = models.PositiveSmallIntegerField()
    slv_ch2_gain_pos = models.PositiveSmallIntegerField()
    slv_ch2_gain_neg = models.PositiveSmallIntegerField()
    slv_ch1_offset_pos = models.PositiveSmallIntegerField()
    slv_ch1_offset_neg = models.PositiveSmallIntegerField()
    slv_ch2_offset_pos = models.PositiveSmallIntegerField()
    slv_ch2_offset_neg = models.PositiveSmallIntegerField()
    slv_common_offset = models.PositiveSmallIntegerField()
    slv_internal_voltage = models.PositiveSmallIntegerField()
    slv_ch1_adc_gain = models.FloatField()
    slv_ch1_adc_offset = models.FloatField()
    slv_ch2_adc_gain = models.FloatField()
    slv_ch2_adc_offset = models.FloatField()
    slv_ch1_comp_gain = models.FloatField()
    slv_ch1_comp_offset = models.FloatField()
    slv_ch2_comp_gain = models.FloatField()
    slv_ch2_comp_offset = models.FloatField()

    def __unicode__(self):
        return "%d - %s" % (self.source.station.number, self.timestamp)

    def station(self):
        return self.source.station.number

class DailyHistogram(models.Model):
    source = models.ForeignKey('Summary')
    type = models.ForeignKey('HistogramType')
    bins = SerializedDataField()
    values = SerializedDataField()

    def __unicode__(self):
        return "%d - %s - %s" % (self.source.station.number,
                                 self.source.date.strftime('%c'), self.type)

    class Meta:
        unique_together = (('source', 'type'),)
        ordering = ('source', 'type')

class DailyDataset(models.Model):
    source = models.ForeignKey('Summary')
    type = models.ForeignKey('DatasetType')
    x = SerializedDataField()
    y = SerializedDataField()

    def __unicode__(self):
        return "%d - %s - %s" % (self.source.station.number,
                                 self.source.date.strftime('%c'), self.type)

    class Meta:
        unique_together = (('source', 'type'),)
        ordering = ('source', 'type')

class HistogramType(models.Model):
    name = models.CharField(max_length=40, unique=True)
    slug = models.CharField(max_length=20, unique=True)
    has_multiple_datasets = models.BooleanField()
    bin_axis_title = models.CharField(max_length=40)
    value_axis_title = models.CharField(max_length=40)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

class DatasetType(models.Model):
    name = models.CharField(max_length=40, unique=True)
    slug = models.CharField(max_length=20, unique=True)
    x_axis_title = models.CharField(max_length=40)
    y_axis_title = models.CharField(max_length=40)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

class GeneratorState(models.Model):
    check_last_run = models.DateTimeField()
    check_is_running = models.BooleanField()
    update_last_run = models.DateTimeField()
    update_is_running = models.BooleanField()