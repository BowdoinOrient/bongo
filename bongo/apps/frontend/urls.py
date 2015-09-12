from django.conf.urls import url
from bongo.apps.frontend import views

urlpatterns = [
    url(r'^$', views.HomeView, name="home"),
    url(r'^article/(?P<slug>\w+)/', views.ArticleView, name="article"),
    url(r'^article/(?P<id>\d+)/', views.ArticleView, name="article"),
    url(r'^author/(?P<id>\d+)/', views.AuthorView, name="author"),
    url(r'^series/(?P<id>\d+)/', views.SeriesView, name="series"),

    # Static views
    url(r'^about/', views.AboutView, name="about"),
    url(r'^contact/', views.ContactView, name="contact"),
    url(r'^subscribe/', views.SubscribeView, name="subscribe"),
    url(r'^ethics/', views.EthicsView, name="ethics"),
    url(r'^advertise/', views.AdvertiseView, name="advertise"),
]
