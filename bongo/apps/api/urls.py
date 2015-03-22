from django.conf.urls import url, include
from bongo.apps.api import endpoints as api
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# routes for every model's create, retrieve, update, delete api endpoints
router.register(r'(?i)series', api.SeriesCrud)
router.register(r'(?i)volume', api.VolumeCrud)
router.register(r'(?i)issue', api.IssueCrud)
router.register(r'(?i)section', api.SectionCrud)
router.register(r'(?i)tag', api.TagCrud)
router.register(r'(?i)job', api.JobCrud)
router.register(r'(?i)creator', api.CreatorCrud)
router.register(r'(?i)text', api.TextCrud)
router.register(r'(?i)video', api.VideoCrud)
router.register(r'(?i)pdf', api.PDFCrud)
router.register(r'(?i)photo', api.PhotoCrud)
router.register(r'(?i)html', api.HTMLCrud)
router.register(r'(?i)pullquote', api.PullquoteCrud)
router.register(r'(?i)post', api.PostCrud)
router.register(r'(?i)alert', api.AlertCrud)
router.register(r'(?i)advertiser', api.AdvertiserCrud)
router.register(r'(?i)ad', api.AdCrud)
router.register(r'(?i)tip', api.TipCrud)
router.register(r'(?i)event', api.EventCrud)
router.register(r'(?i)scheduledpost', api.ScheduledPostCrud)


# routes for every model's restricted api (retrieve only)
router.register(r'(?i)series', api.SeriesCrudRestricted)
router.register(r'(?i)volume', api.VolumeCrudRestricted)
router.register(r'(?i)issue', api.IssueCrudRestricted)
router.register(r'(?i)section', api.SectionCrudRestricted)
router.register(r'(?i)tag', api.TagCrudRestricted)
router.register(r'(?i)job', api.JobCrudRestricted)
router.register(r'(?i)creator', api.CreatorCrudRestricted)
router.register(r'(?i)text', api.TextCrudRestricted)
router.register(r'(?i)video', api.VideoCrudRestricted)
router.register(r'(?i)pdf', api.PDFCrudRestricted)
router.register(r'(?i)photo', api.PhotoCrudRestricted)
router.register(r'(?i)html', api.HTMLCrudRestricted)
router.register(r'(?i)pullquote', api.PullquoteCrudRestricted)
router.register(r'(?i)post', api.PostCrudRestricted)
router.register(r'(?i)alert', api.AlertCrudRestricted)
router.register(r'(?i)advertiser', api.AdvertiserCrudRestricted)
router.register(r'(?i)ad', api.AdCrudRestricted)
router.register(r'(?i)tip', api.TipCrudRestricted)
router.register(r'(?i)event', api.EventCrudRestricted)
router.register(r'(?i)scheduledpost', api.ScheduledPostCrudRestricted)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]