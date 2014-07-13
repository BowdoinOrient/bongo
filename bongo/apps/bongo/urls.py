from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from bongo.apps.bongo.api import ad, advertiser, alert, content, creator, event, html, issue, job, pdf, photo, post, pullquote, scheduledpost, section, series, tag, text, tip, video, volume

urlpatterns = patterns('',
    url(r'ad/$', ad.AdList.as_view()),
    url(r'ad/(?P<pk>[0-9]+)/$', ad.AdDetail.as_view()),

    url(r'advertiser/$', advertiser.AdvertiserList.as_view()),
    url(r'advertiser/(?P<pk>[0-9]+)/$', advertiser.AdvertiserDetail.as_view()),

    url(r'alert/$', alert.AlertList.as_view()),
    url(r'alert/(?P<pk>[0-9]+)/$', alert.AlertDetail.as_view()),

    url(r'content/$', content.ContentList.as_view()),
    url(r'content/(?P<pk>[0-9]+)/$', content.ContentDetail.as_view()),

    url(r'creator/$', creator.CreatorList.as_view()),
    url(r'creator/(?P<pk>[0-9]+)/$', creator.CreatorDetail.as_view()),

    url(r'event/$', event.EventList.as_view()),
    url(r'event/(?P<pk>[0-9]+)/$', event.EventDetail.as_view()),

    url(r'html/$', html.HTMLList.as_view()),
    url(r'html/(?P<pk>[0-9]+)/$', html.HTMLDetail.as_view()),

    url(r'issue/$', issue.IssueList.as_view()),
    url(r'issue/(?P<pk>[0-9]+)/$', issue.IssueDetail.as_view()),

    url(r'job/$', job.JobList.as_view()),
    url(r'job/(?P<pk>[0-9]+)/$', job.JobDetail.as_view()),

    url(r'pdf/$', pdf.PDFList.as_view()),
    url(r'pdf/(?P<pk>[0-9]+)/$', pdf.PDFDetail.as_view()),

    url(r'photo/$', photo.PhotoList.as_view()),
    url(r'photo/(?P<pk>[0-9]+)/$', photo.PhotoDetail.as_view()),

    url(r'post/$', post.PostList.as_view()),
    url(r'post/(?P<pk>[0-9]+)/$', post.PostDetail.as_view()),

    url(r'pullquote/$', pullquote.PullquoteList.as_view()),
    url(r'pullquote/(?P<pk>[0-9]+)/$', pullquote.PullquoteDetail.as_view()),

    url(r'scheduledpost/$', scheduledpost.ScheduledPostList.as_view()),
    url(r'scheduledpost/(?P<pk>[0-9]+)/$', scheduledpost.ScheduledPostDetail.as_view()),

    url(r'section/$', section.SectionList.as_view()),
    url(r'section/(?P<pk>[0-9]+)/$', section.SectionDetail.as_view()),

    url(r'series/$', series.SeriesList.as_view()),
    url(r'series/(?P<pk>[0-9]+)/$', series.SeriesDetail.as_view()),

    url(r'tag/$', tag.TagList.as_view()),
    url(r'tag/(?P<pk>[0-9]+)/$', tag.TagDetail.as_view()),

    url(r'text/$', text.TextList.as_view()),
    url(r'text/(?P<pk>[0-9]+)/$', text.TextDetail.as_view()),

    url(r'tip/$', tip.TipList.as_view()),
    url(r'tip/(?P<pk>[0-9]+)/$', tip.TipDetail.as_view()),

    url(r'video/$', video.VideoList.as_view()),
    url(r'video/(?P<pk>[0-9]+)/$', video.VideoDetail.as_view()),

    url(r'volume/$', volume.VolumeList.as_view()),
    url(r'volume/(?P<pk>[0-9]+)/$', volume.VolumeDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)