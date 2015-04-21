from bongo.apps.bongo.models import Event
from bongo.apps.api.serializers.event import EventSerializer
from rest_framework import viewsets, permissions, filters

class EventCrud(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class EventCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (filters.OrderingFilter,)