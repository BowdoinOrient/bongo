from bongo.apps.bongo.models import PDF
from bongo.apps.api.serializers.pdf import PDFSerializer
from rest_framework import viewsets, permissions, filters

class PDFCrud(viewsets.ModelViewSet):
    queryset = PDF.objects.all()
    serializer_class = PDFSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.OrderingFilter,)

class PDFCrudRestricted(viewsets.ReadOnlyModelViewSet):
    queryset = PDF.objects.all()
    serializer_class = PDFSerializer
    filter_backends = (filters.OrderingFilter,)