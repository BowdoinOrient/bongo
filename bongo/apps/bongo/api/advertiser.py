from bongo.apps.bongo.models import Advertiser
from bongo.apps.bongo.serializers import AdvertiserSerializer
from rest_framework import generics

class AdvertiserList(generics.ListCreateAPIView):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer

class AdvertiserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer