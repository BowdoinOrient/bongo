from bongo.apps.bongo.models import Pullquote
from bongo.apps.bongo.serializers import PullquoteSerializer
from rest_framework import generics

class PullquoteList(generics.ListCreateAPIView):
    queryset = Pullquote.objects.all()
    serializer_class = PullquoteSerializer

class PullquoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pullquote.objects.all()
    serializer_class = PullquoteSerializer