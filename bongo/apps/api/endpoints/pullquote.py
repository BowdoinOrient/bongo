from bongo.apps.bongo.models import Pullquote
from bongo.apps.api.serializers.pullquote import PullquoteSerializer
from rest_framework import viewsets, permissions, filters

class PullquoteCrud(viewsets.ModelViewSet):
    queryset = Pullquote.objects.all()
    serializer_class = PullquoteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class PullquoteCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Pullquote.objects.all()
    serializer_class = PullquoteSerializer
    filter_backends = (filters.OrderingFilter,)