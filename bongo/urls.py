from django.conf.urls import patterns, include, url
from django.contrib import admin
from bongo.apps.bongo import urls as api_urls

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include(api_urls)),

)
