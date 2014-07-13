from bongo.apps.bongo.models import Job
from bongo.apps.bongo.serializers import JobSerializer
from rest_framework import generics

class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer