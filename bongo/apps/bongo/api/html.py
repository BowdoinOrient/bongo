from bongo.apps.bongo.models import HTML
from bongo.apps.bongo.serializers import HTMLSerializer
from rest_framework import generics

class HTMLList(generics.ListCreateAPIView):
    queryset = HTML.objects.all()
    serializer_class = HTMLSerializer

class HTMLDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HTML.objects.all()
    serializer_class = HTMLSerializer