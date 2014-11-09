from django.conf.urls import patterns, url
from bongo.apps.frontend import views

urlpatterns = patterns('',
    url(r'', views.HomeView, name="home"),
    url(r'article/', views.ArticleView, name="article"),
    url(r'author/', views.AuthorView, name="author"),
    url(r'series/', views.SeriesView, name="series"),

    # Static views
    
)