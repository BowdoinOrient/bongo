from bongo.apps.bongo.models import Ad
from bongo.apps.api.serializers.ad import AdSerializer
from rest_framework import viewsets, permissions, filters

class AdCrud(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class AdCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = (filters.OrderingFilter,)