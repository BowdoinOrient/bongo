from django.conf.urls import patterns, include, url
from django.contrib import admin
from bongo.apps.api import urls as api_urls
from bongo.apps.frontend import urls as frontend_urls

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include(api_urls)),
    url(r'^', include(frontend_urls))

)
