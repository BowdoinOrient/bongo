from bongo.apps.bongo.models import Tip
from bongo.apps.bongo.serializers import TipSerializer
from rest_framework import generics

class TipList(generics.ListCreateAPIView):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer

class TipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer
