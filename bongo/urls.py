from django.conf.urls import patterns, include, url
from django.contrib import admin
from bongo.apps.bongo import urls as api_urls
from django.conf import settings

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include(api_urls)),

)

if settings.DEBUG:
    urlpatterns += (url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),)

handler404 = 'bongo.apps.bongo.views.custom404'