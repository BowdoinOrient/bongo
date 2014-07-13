from bongo.apps.bongo.models import Tag
from bongo.apps.bongo.serializers import TagSerializer
from rest_framework import generics

class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer