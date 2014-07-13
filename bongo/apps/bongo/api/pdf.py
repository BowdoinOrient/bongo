from bongo.apps.bongo.models import PDF
from bongo.apps.bongo.serializers import PDFSerializer
from rest_framework import generics

class PDFList(generics.ListCreateAPIView):
    queryset = PDF.objects.all()
    serializer_class = PDFSerializer

class PDFDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PDF.objects.all()
    serializer_class = PDFSerializer