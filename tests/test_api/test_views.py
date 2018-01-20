from django.test import Client, TestCase
from django.urls import reverse

from ..factories.histograms_factories import ConfigurationFactory
from ..factories.inforecords_factories import StationFactory


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.station = StationFactory(number=1, cluster__number=0, cluster__country__number=0)
        self.config = ConfigurationFactory(source__station=self.station)

    def get_json(self, url):
        """Get url and check if the response is OK and valid json"""
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        return response.json()

    def not_found(self, url):
        """Get url and check if the response is NOT FOUND"""
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_man(self):
        self.get_json(reverse('api:man'))

    def test_station(self):
        kwargs = {'station_number': self.station.number}
        self.get_json(reverse('api:station', kwargs=kwargs))
        self.get_json(reverse('api:has_data', kwargs=kwargs))
        self.get_json(reverse('api:has_weather', kwargs=kwargs))
        self.get_json(reverse('api:num_events', kwargs=kwargs))
        self.get_json(reverse('api:config', kwargs=kwargs))

        kwargs.update({'year': 2011})
        self.get_json(reverse('api:has_data', kwargs=kwargs))
        self.get_json(reverse('api:has_weather', kwargs=kwargs))
        self.get_json(reverse('api:num_events', kwargs=kwargs))

        kwargs.update({'month': 9})
        self.get_json(reverse('api:has_data', kwargs=kwargs))
        self.get_json(reverse('api:has_weather', kwargs=kwargs))
        self.get_json(reverse('api:num_events', kwargs=kwargs))

        kwargs.update({'day': 5})
        self.get_json(reverse('api:station', kwargs=kwargs))
        self.get_json(reverse('api:has_data', kwargs=kwargs))
        self.get_json(reverse('api:has_weather', kwargs=kwargs))
        self.get_json(reverse('api:num_events', kwargs=kwargs))

        kwargs.update({'hour': 14})
        self.get_json(reverse('api:num_events', kwargs=kwargs))

        config_date = self.config.source.date
        kwargs = {
            'station_number': self.station.number,
            'year': config_date.year,
            'month': config_date.month,
            'day': config_date.day
        }
        self.get_json(reverse('api:config', kwargs=kwargs))

    def test_stations(self):
        self.get_json(reverse('api:stations'))
        self.get_json(reverse('api:data_stations'))
        self.get_json(reverse('api:weather_stations'))

        kwargs = {'year': 2011}
        self.get_json(reverse('api:data_stations', kwargs=kwargs))
        self.get_json(reverse('api:weather_stations', kwargs=kwargs))

        kwargs.update({'month': 9})
        self.get_json(reverse('api:data_stations', kwargs=kwargs))
        self.get_json(reverse('api:weather_stations', kwargs=kwargs))

        kwargs.update({'day': 5})
        self.get_json(reverse('api:data_stations', kwargs=kwargs))
        self.get_json(reverse('api:weather_stations', kwargs=kwargs))

    def test_subclusters(self):
        self.get_json(reverse('api:subclusters'))
        kwargs = {'subcluster_number': self.station.cluster.number}
        self.get_json(reverse('api:stations', kwargs=kwargs))

        kwargs = {'subcluster_number': 1337}
        self.not_found(reverse('api:stations', kwargs=kwargs))

    def test_clusters(self):
        self.get_json(reverse('api:clusters'))
        kwargs = {'cluster_number': self.station.cluster.number}
        self.get_json(reverse('api:subclusters', kwargs=kwargs))

        kwargs = {'cluster_number': 1337}
        self.not_found(reverse('api:subclusters', kwargs=kwargs))

    def test_countries(self):
        self.get_json(reverse('api:countries'))
        kwargs = {'country_number': self.station.cluster.country.number}
        self.get_json(reverse('api:clusters', kwargs=kwargs))

        kwargs = {'country_number': 1337}
        self.not_found(reverse('api:clusters', kwargs=kwargs))
