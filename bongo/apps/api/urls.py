from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .endpoints.series import SeriesCrud, SeriesCrudRestricted
from .endpoints.volume import VolumeCrud, VolumeCrudRestricted
from .endpoints.issue import IssueCrud, IssueCrudRestricted
from .endpoints.section import SectionCrud, SectionCrudRestricted
from .endpoints.tag import TagCrud, TagCrudRestricted
from .endpoints.job import JobCrud, JobCrudRestricted
from .endpoints.creator import CreatorCrud, CreatorCrudRestricted
from .endpoints.text import TextCrud, TextCrudRestricted
from .endpoints.video import VideoCrud, VideoCrudRestricted
from .endpoints.pdf import PDFCrud, PDFCrudRestricted
from .endpoints.photo import PhotoCrud, PhotoCrudRestricted
from .endpoints.html import HTMLCrud, HTMLCrudRestricted
from .endpoints.pullquote import PullquoteCrud, PullquoteCrudRestricted
from .endpoints.post import PostCrud, PostCrudRestricted
from .endpoints.alert import AlertCrud, AlertCrudRestricted
from .endpoints.advertiser import AdvertiserCrud, AdvertiserCrudRestricted
from .endpoints.ad import AdCrud, AdCrudRestricted
from .endpoints.tip import TipCrud, TipCrudRestricted
from .endpoints.event import EventCrud, EventCrudRestricted
from .endpoints.scheduledpost import ScheduledPostCrud, ScheduledPostCrudRestricted
from .endpoints.search import search
from .endpoints.root import api_root

router = DefaultRouter()

# routes for every model's create, retrieve, update, delete api endpoints
router.register(r'(?i)series', SeriesCrud)
router.register(r'(?i)volume', VolumeCrud)
router.register(r'(?i)issue', IssueCrud)
router.register(r'(?i)section', SectionCrud)
router.register(r'(?i)tag', TagCrud)
router.register(r'(?i)job', JobCrud)
router.register(r'(?i)creator', CreatorCrud)
router.register(r'(?i)text', TextCrud)
router.register(r'(?i)video', VideoCrud)
router.register(r'(?i)pdf', PDFCrud)
router.register(r'(?i)photo', PhotoCrud)
router.register(r'(?i)html', HTMLCrud)
router.register(r'(?i)pullquote', PullquoteCrud)
router.register(r'(?i)post', PostCrud)
router.register(r'(?i)alert', AlertCrud)
router.register(r'(?i)advertiser', AdvertiserCrud)
router.register(r'(?i)ad', AdCrud)
router.register(r'(?i)tip', TipCrud)
router.register(r'(?i)event', EventCrud)
router.register(r'(?i)scheduledpost', ScheduledPostCrud)


# routes for every model's restricted api (retrieve only)
router.register(r'(?i)series', SeriesCrudRestricted)
router.register(r'(?i)volume', VolumeCrudRestricted)
router.register(r'(?i)issue', IssueCrudRestricted)
router.register(r'(?i)section', SectionCrudRestricted)
router.register(r'(?i)tag', TagCrudRestricted)
router.register(r'(?i)job', JobCrudRestricted)
router.register(r'(?i)creator', CreatorCrudRestricted)
router.register(r'(?i)text', TextCrudRestricted)
router.register(r'(?i)video', VideoCrudRestricted)
router.register(r'(?i)pdf', PDFCrudRestricted)
router.register(r'(?i)photo', PhotoCrudRestricted)
router.register(r'(?i)html', HTMLCrudRestricted)
router.register(r'(?i)pullquote', PullquoteCrudRestricted)
router.register(r'(?i)post', PostCrudRestricted)
router.register(r'(?i)alert', AlertCrudRestricted)
router.register(r'(?i)advertiser', AdvertiserCrudRestricted)
router.register(r'(?i)ad', AdCrudRestricted)
router.register(r'(?i)tip', TipCrudRestricted)
router.register(r'(?i)event', EventCrudRestricted)
router.register(r'(?i)scheduledpost', ScheduledPostCrudRestricted)

urlpatterns = [
    url(r'^$', api_root),
    url(r'^', include(router.urls)),
    url(r'(?i)search/', search, name="search"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]