from bongo.apps.bongo.models import *
from bongo.apps.bongo.serializers import *
from rest_framework import generics


class SeriesList(generics.ListCreateAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer

class SeriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer