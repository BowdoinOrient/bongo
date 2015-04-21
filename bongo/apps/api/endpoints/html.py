from bongo.apps.bongo.models import HTML
from bongo.apps.api.serializers.html import HTMLSerializer
from rest_framework import viewsets, permissions, filters

class HTMLCrud(viewsets.ModelViewSet):
    queryset = HTML.objects.all()
    serializer_class = HTMLSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class HTMLCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = HTML.objects.all()
    serializer_class = HTMLSerializer
    filter_backends = (filters.OrderingFilter,)