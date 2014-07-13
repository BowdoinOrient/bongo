from bongo.apps.bongo.models import Volume
from bongo.apps.bongo.serializers import VolumeSerializer
from rest_framework import generics


class VolumeList(generics.ListCreateAPIView):
    queryset =Volume.objects.all()
    serializer_class = VolumeSerializer

class VolumeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer