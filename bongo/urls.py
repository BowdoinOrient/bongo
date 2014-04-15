from django.conf.urls import patterns, include, url
from django.contrib import admin
from bongo.apps.bongo.api import *
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(PostResource())

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
