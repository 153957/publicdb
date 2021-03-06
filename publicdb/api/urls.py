from django.conf.urls import url

from . import views

app_name = 'api'
urlpatterns = [
    url(r'^$', views.man, name="man"),

    url(r'^network/status/$', views.network_status),

    url(r'^stations/$', views.stations, name="stations"),
    url(r'^subclusters/$', views.subclusters, name="subclusters"),
    url(r'^clusters/$', views.clusters, name="clusters"),
    url(r'^countries/$', views.countries, name="countries"),

    url(r'^subclusters/(?P<subcluster_number>\d+)/$', views.stations, name="stations"),
    url(r'^clusters/(?P<cluster_number>\d+)/$', views.subclusters, name="subclusters"),
    url(r'^countries/(?P<country_number>\d+)/$', views.clusters, name="clusters"),

    url(r'^stations/data/$', views.stations_with_data, {'type': 'events'}, name="data_stations"),
    url(r'^stations/data/(?P<year>\d{4})/$', views.stations_with_data, {'type': 'events'}, name="data_stations"),
    url(r'^stations/data/(?P<year>\d{4})/(?P<month>\d{1,2})/$', views.stations_with_data, {'type': 'events'}, name="data_stations"),
    url(r'^stations/data/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', views.stations_with_data, {'type': 'events'}, name="data_stations"),
    url(r'^stations/weather/$', views.stations_with_data, {'type': 'weather'}, name="weather_stations"),
    url(r'^stations/weather/(?P<year>\d{4})/$', views.stations_with_data, {'type': 'weather'}, name="weather_stations"),
    url(r'^stations/weather/(?P<year>\d{4})/(?P<month>\d{1,2})/$', views.stations_with_data, {'type': 'weather'}, name="weather_stations"),
    url(r'^stations/weather/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', views.stations_with_data, {'type': 'weather'}, name="weather_stations"),
    url(r'^stations/singles/$', views.stations_with_data, {'type': 'singles'}, name="singles_stations"),
    url(r'^stations/singles/(?P<year>\d{4})/$', views.stations_with_data, {'type': 'singles'}, name="singles_stations"),
    url(r'^stations/singles/(?P<year>\d{4})/(?P<month>\d{1,2})/$', views.stations_with_data, {'type': 'singles'}, name="singles_stations"),
    url(r'^stations/singles/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', views.stations_with_data, {'type': 'singles'}, name="singles_stations"),

    url(r'^station/(?P<station_number>\d+)/$', views.station, name="station"),
    url(r'^station/(?P<station_number>\d+)/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', views.station, name="station"),

    url(r'^station/(?P<station_number>\d+)/data/$', views.has_data, {'type': 'events'}, name="has_data"),
    url(r'^station/(?P<station_number>\d+)/data/(?P<year>\d{4})/$', views.has_data, {'type': 'events'}, name="has_data"),
    url(r'^station/(?P<station_number>\d+)/data/(?P<year>\d{4})/(?P<month>\d{1,2})/$', views.has_data, {'type': 'events'}, name="has_data"),
    url(r'^station/(?P<station_number>\d+)/data/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', views.has_data, {'type': 'events'}, name="has_data"),
    url(r'^station/(?P<station_number>\d+)/weather/$', views.has_data, {'type': 'weather'}, name="has_weather"),
    url(r'^station/(?P<station_number>\d+)/weather/(?P<year>\d{4})/$', views.has_data, {'type': 'weather'}, name="has_weather"),
    url(r'^station/(?P<station_number>\d+)/weather/(?P<year>\d{4})/(?P<month>\d{1,2})/$', views.has_data, {'type': 'weather'}, name="has_weather"),
    url(r'^station/(?P<station_number>\d+)/weather/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', views.has_data, {'type': 'weather'}, name="has_weather"),
    url(r'^station/(?P<station_number>\d+)/singles/$', views.has_data, {'type': 'singles'}, name="has_singles"),
    url(r'^station/(?P<station_number>\d+)/singles/(?P<year>\d{4})/$', views.has_data, {'type': 'singles'}, name="has_singles"),
    url(r'^station/(?P<station_number>\d+)/singles/(?P<year>\d{4})/(?P<month>\d{1,2})/$', views.has_data, {'type': 'singles'}, name="has_singles"),
    url(r'^station/(?P<station_number>\d+)/singles/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', views.has_data, {'type': 'singles'}, name="has_singles"),
    url(r'^station/(?P<station_number>\d+)/config/$', views.config, name="config"),
    url(r'^station/(?P<station_number>\d+)/config/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', views.config, name="config"),

    url(r'^station/(?P<station_number>\d+)/num_events/$', views.num_events, name="num_events"),
    url(r'^station/(?P<station_number>\d+)/num_events/(?P<year>\d{4})/$', views.num_events, name="num_events"),
    url(r'^station/(?P<station_number>\d+)/num_events/(?P<year>\d{4})/(?P<month>\d{1,2})/$', views.num_events, name="num_events"),
    url(r'^station/(?P<station_number>\d+)/num_events/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', views.num_events, name="num_events"),
    url(r'^station/(?P<station_number>\d+)/num_events/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<hour>\d+)/$', views.num_events, name="num_events"),

    url(r'^station/(?P<station_number>\d+)/trace/(?P<ext_timestamp>\d+)/$', views.get_event_traces, name="event_traces"),
]
