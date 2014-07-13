from bongo.apps.bongo.models import Event
from bongo.apps.bongo.serializers import EventSerializer
from rest_framework import generics


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer