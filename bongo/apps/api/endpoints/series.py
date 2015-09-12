from bongo.apps.bongo.models import Series
from bongo.apps.api.serializers.series import SeriesSerializer
from rest_framework import viewsets, permissions, filters


class SeriesCrud(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)


class SeriesCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    filter_backends = (filters.OrderingFilter,)
