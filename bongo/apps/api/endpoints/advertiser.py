from bongo.apps.bongo.models import Advertiser
from bongo.apps.api.serializers.advertiser import AdvertiserSerializer
from rest_framework import viewsets, permissions, filters


class AdvertiserCrud(viewsets.ModelViewSet):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)


class AdvertiserCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer
    filter_backends = (filters.OrderingFilter,)
