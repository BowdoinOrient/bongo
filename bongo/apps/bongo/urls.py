from django.conf.urls import patterns, url, include
from bongo.apps.bongo import api
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# routes for every model's create, retrieve, update, delete api endpoints
router.register(r'series', api.SeriesCrud)
router.register(r'volume', api.VolumeCrud)
router.register(r'issue', api.IssueCrud)
router.register(r'section', api.SectionCrud)
router.register(r'tag', api.TagCrud)
router.register(r'job', api.JobCrud)
router.register(r'creator', api.CreatorCrud)
router.register(r'text', api.TextCrud)
router.register(r'video', api.VideoCrud)
router.register(r'pdf', api.PDFCrud)
router.register(r'photo', api.PhotoCrud)
router.register(r'html', api.HTMLCrud)
router.register(r'pullquote', api.PullquoteCrud)
router.register(r'post', api.PostCrud)
router.register(r'alert', api.AlertCrud)
router.register(r'advertiser', api.AdvertiserCrud)
router.register(r'ad', api.AdCrud)
router.register(r'tip', api.TipCrud)
router.register(r'event', api.EventCrud)
router.register(r'scheduledpost', api.ScheduledPostCrud)


# routes for every model's restricted api (retrieve only)
router.register(r'series', api.SeriesCrudRestricted)
router.register(r'volume', api.VolumeCrudRestricted)
router.register(r'issue', api.IssueCrudRestricted)
router.register(r'section', api.SectionCrudRestricted)
router.register(r'tag', api.TagCrudRestricted)
router.register(r'job', api.JobCrudRestricted)
router.register(r'creator', api.CreatorCrudRestricted)
router.register(r'text', api.TextCrudRestricted)
router.register(r'video', api.VideoCrudRestricted)
router.register(r'pdf', api.PDFCrudRestricted)
router.register(r'photo', api.PhotoCrudRestricted)
router.register(r'html', api.HTMLCrudRestricted)
router.register(r'pullquote', api.PullquoteCrudRestricted)
router.register(r'post', api.PostCrudRestricted)
router.register(r'alert', api.AlertCrudRestricted)
router.register(r'advertiser', api.AdvertiserCrudRestricted)
router.register(r'ad', api.AdCrudRestricted)
router.register(r'tip', api.TipCrudRestricted)
router.register(r'event', api.EventCrudRestricted)
router.register(r'scheduledpost', api.ScheduledPostCrudRestricted)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)