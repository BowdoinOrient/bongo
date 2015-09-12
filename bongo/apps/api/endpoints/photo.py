from bongo.apps.bongo.models import Photo
from bongo.apps.api.serializers.photo import PhotoSerializer
from rest_framework import viewsets, permissions, filters


class PhotoCrud(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)


class PhotoCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    filter_backends = (filters.OrderingFilter,)
