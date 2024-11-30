from rest_framework import generics
from .serializers import JobSerializer
from .models import Jobs



class job_list(generics.ListAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer
    
    
class job_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'id'