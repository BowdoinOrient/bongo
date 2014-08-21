from bongo.apps.bongo.models import *
from bongo.apps.bongo.serializers import *
from rest_framework import viewsets, permissions
from rest_framework.decorators import action, link
from rest_framework.response import Response
from django.core import serializers


""" I know this is a gigantic mess - I'm searching for a better way.
    Haven't found it yet, obviously.
"""

class SeriesCrud(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SeriesCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer

class VolumeCrud(viewsets.ModelViewSet):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class VolumeCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer

class IssueCrud(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class IssueCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    @link()
    def latest(self, request, pk=None):
        return Response(IssueSerializer(Issue.objects.order_by("-issue_date")[:1]).data[0])

class LatestIssueCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Issue.objects.order_by("-issue_date")[:1]
    serializer_class = IssueSerializer

class SectionCrud(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SectionCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

    @link()
    def latest(self, request, pk=None):
        if 'limit' in request.GET:
            l = request.GET['limit']
        else:
            l = 10

        posts = Post.objects.filter(section_id__exact=pk).order_by("-published")[:l]

        serializedPosts = []
        for post in posts:
            print PostSerializer(post).data
            serializedPosts.append(PostSerializer(post).data)

        return Response(serializedPosts)

class TagCrud(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class TagCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class JobCrud(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class JobCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class CreatorCrud(viewsets.ModelViewSet):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CreatorCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer

class ContentCrud(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ContentCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class TextCrud(viewsets.ModelViewSet):
    queryset = Text.objects.all()
    serializer_class = TextSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class TextCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Text.objects.all()
    serializer_class = TextSerializer

class VideoCrud(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class VideoCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class PDFCrud(viewsets.ModelViewSet):
    queryset = PDF.objects.all()
    serializer_class = PDFSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class PDFCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = PDF.objects.all()
    serializer_class = PDFSerializer

class PhotoCrud(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class PhotoCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class HTMLCrud(viewsets.ModelViewSet):
    queryset = HTML.objects.all()
    serializer_class = HTMLSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class HTMLCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = HTML.objects.all()
    serializer_class = HTMLSerializer

class PullquoteCrud(viewsets.ModelViewSet):
    queryset = Pullquote.objects.all()
    serializer_class = PullquoteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class PullquoteCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Pullquote.objects.all()
    serializer_class = PullquoteSerializer

class PostCrud(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class PostCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class AlertCrud(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class AlertCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

class AdvertiserCrud(viewsets.ModelViewSet):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class AdvertiserCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer

class AdCrud(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class AdCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

class TipCrud(viewsets.ModelViewSet):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class TipCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer

class EventCrud(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class EventCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class ScheduledPostCrud(viewsets.ModelViewSet):
    queryset = ScheduledPost.objects.all()
    serializer_class = ScheduledPostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ScheduledPostCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = ScheduledPost.objects.all()
    serializer_class = ScheduledPostSerializer