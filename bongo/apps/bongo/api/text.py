from bongo.apps.bongo.models import Text
from bongo.apps.bongo.serializers import TextSerializer
from rest_framework import generics

class TextList(generics.ListCreateAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer

class TextDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer