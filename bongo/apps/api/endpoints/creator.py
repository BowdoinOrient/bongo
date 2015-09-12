from bongo.apps.bongo.models import Creator
from bongo.apps.api.serializers.creator import CreatorSerializer
from rest_framework import viewsets, permissions, filters


class CreatorCrud(viewsets.ModelViewSet):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)


class CreatorCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer
    filter_backends = (filters.OrderingFilter,)
