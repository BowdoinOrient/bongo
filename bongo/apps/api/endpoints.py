from bongo.apps.bongo.models import *
from serializers import *
from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import link
from rest_framework.response import Response


""" I know this is a gigantic mess - I'm searching for a better way.
    Haven't found it yet, obviously.
"""

class SeriesCrud(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class SeriesCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    filter_backends = (filters.OrderingFilter,)

class VolumeCrud(viewsets.ModelViewSet):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class VolumeCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer
    filter_backends = (filters.OrderingFilter,)

class IssueCrud(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class IssueCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    filter_backends = (filters.OrderingFilter,)

class SectionCrud(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class SectionCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    filter_backends = (filters.OrderingFilter,)

    @link()
    def posts(self, request, pk=None):
        if 'limit' in request.GET:
            l = request.GET['limit']
        else:
            l = 10

        if 'ordering' in request.GET:
            s = request.GET["ordering"]
        else:
            s = "-published"

        posts = Post.objects.filter(section_id__exact=pk).order_by(s)[:l]

        serializedPosts = []
        for post in posts:
            serializedPosts.append(PostSerializer(post).data)

        return Response(serializedPosts)

class TagCrud(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class TagCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = (filters.OrderingFilter,)

class JobCrud(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class JobCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = (filters.OrderingFilter,)

class CreatorCrud(viewsets.ModelViewSet):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class CreatorCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer
    filter_backends = (filters.OrderingFilter,)

class TextCrud(viewsets.ModelViewSet):
    queryset = Text.objects.all()
    serializer_class = TextSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class TextCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Text.objects.all()
    serializer_class = TextSerializer
    filter_backends = (filters.OrderingFilter,)

class VideoCrud(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class VideoCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = (filters.OrderingFilter,)

class PDFCrud(viewsets.ModelViewSet):
    queryset = PDF.objects.all()
    serializer_class = PDFSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class PDFCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = PDF.objects.all()
    serializer_class = PDFSerializer
    filter_backends = (filters.OrderingFilter,)

class PhotoCrud(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class PhotoCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    filter_backends = (filters.OrderingFilter,)

class HTMLCrud(viewsets.ModelViewSet):
    queryset = HTML.objects.all()
    serializer_class = HTMLSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class HTMLCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = HTML.objects.all()
    serializer_class = HTMLSerializer
    filter_backends = (filters.OrderingFilter,)

class PullquoteCrud(viewsets.ModelViewSet):
    queryset = Pullquote.objects.all()
    serializer_class = PullquoteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class PullquoteCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Pullquote.objects.all()
    serializer_class = PullquoteSerializer
    filter_backends = (filters.OrderingFilter,)

class PostCrud(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class PostCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (filters.OrderingFilter,)

class AlertCrud(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class AlertCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    filter_backends = (filters.OrderingFilter,)

class AdvertiserCrud(viewsets.ModelViewSet):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class AdvertiserCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer
    filter_backends = (filters.OrderingFilter,)

class AdCrud(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class AdCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = (filters.OrderingFilter,)

class TipCrud(viewsets.ModelViewSet):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class TipCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer
    filter_backends = (filters.OrderingFilter,)

class EventCrud(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class EventCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (filters.OrderingFilter,)

class ScheduledPostCrud(viewsets.ModelViewSet):
    queryset = ScheduledPost.objects.all()
    serializer_class = ScheduledPostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class ScheduledPostCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = ScheduledPost.objects.all()
    serializer_class = ScheduledPostSerializer
    filter_backends = (filters.OrderingFilter,)