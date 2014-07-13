from bongo.apps.bongo.models import Alert
from bongo.apps.bongo.serializers import AlertSerializer
from rest_framework import generics

class AlertList(generics.ListCreateAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

class AlertDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer