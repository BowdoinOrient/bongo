from bongo.apps.bongo.models import Text
from bongo.apps.api.serializers.text import TextSerializer
from rest_framework import viewsets, permissions, filters


class TextCrud(viewsets.ModelViewSet):
    queryset = Text.objects.all()
    serializer_class = TextSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)


class TextCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Text.objects.all()
    serializer_class = TextSerializer
    filter_backends = (filters.OrderingFilter,)
