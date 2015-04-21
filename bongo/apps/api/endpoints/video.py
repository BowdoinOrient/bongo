from bongo.apps.bongo.models import Video
from bongo.apps.api.serializers.video import VideoSerializer
from rest_framework import viewsets, permissions, filters

class VideoCrud(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class VideoCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = (filters.OrderingFilter,)