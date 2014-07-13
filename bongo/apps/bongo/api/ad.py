from bongo.apps.bongo.models import Ad
from bongo.apps.bongo.serializers import AdSerializer
from rest_framework import generics

class AdList(generics.ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

class AdDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
