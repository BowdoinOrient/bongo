from bongo.apps.bongo.models import Tip
from bongo.apps.api.serializers.tip import TipSerializer
from rest_framework import viewsets, permissions, filters

class TipCrud(viewsets.ModelViewSet):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class TipCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer
    filter_backends = (filters.OrderingFilter,)