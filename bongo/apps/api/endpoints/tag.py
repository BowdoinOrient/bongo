from bongo.apps.bongo.models import Tag
from bongo.apps.api.serializers.tag import TagSerializer
from rest_framework import viewsets, permissions, filters

class TagCrud(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class TagCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = (filters.OrderingFilter,)