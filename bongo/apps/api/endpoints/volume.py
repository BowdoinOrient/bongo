from bongo.apps.bongo.models import Volume
from bongo.apps.api.serializers.volume import VolumeSerializer
from rest_framework import viewsets, permissions, filters


class VolumeCrud(viewsets.ModelViewSet):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)


class VolumeCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer
    filter_backends = (filters.OrderingFilter,)
