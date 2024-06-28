from rest_framework import viewsets
from .models import PatientData
from .serializers import PatientDataSerializer

class PatientDataViewSet(viewsets.ModelViewSet):
    queryset = PatientData.objects.all()
    serializer_class = PatientDataSerializer
