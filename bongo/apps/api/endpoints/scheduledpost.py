from bongo.apps.bongo.models import ScheduledPost
from bongo.apps.api.serializers.scheduledpost import ScheduledPostSerializer
from rest_framework import viewsets, permissions, filters


class ScheduledPostCrud(viewsets.ModelViewSet):
    queryset = ScheduledPost.objects.all()
    serializer_class = ScheduledPostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)


class ScheduledPostCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = ScheduledPost.objects.all()
    serializer_class = ScheduledPostSerializer
    filter_backends = (filters.OrderingFilter,)
