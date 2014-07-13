from bongo.apps.bongo.models import Issue
from bongo.apps.bongo.serializers import IssueSerializer
from rest_framework import generics

class IssueList(generics.ListCreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class IssueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Issue.objects.all()