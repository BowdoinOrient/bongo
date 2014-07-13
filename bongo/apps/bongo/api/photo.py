from bongo.apps.bongo.models import Photo
from bongo.apps.bongo.serializers import PhotoSerializer
from rest_framework import generics

class PhotoList(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer