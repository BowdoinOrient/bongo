from bongo.apps.bongo.models import Section
from bongo.apps.bongo.serializers import SectionSerializer
from rest_framework import generics

class SectionList(generics.ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class SectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer