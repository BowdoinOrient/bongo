from bongo.apps.bongo.models import Creator
from bongo.apps.bongo.serializers import CreatorSerializer
from rest_framework import generics


class CreatorList(generics.ListCreateAPIView):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer

class CreatorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer
