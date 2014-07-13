from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from bongo.apps.bongo import api

urlpatterns = patterns('',
    url(r'series/$', api.SeriesList.as_view()),
    url(r'series/(?P<pk>[0-9]+)/$', api.SeriesDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)