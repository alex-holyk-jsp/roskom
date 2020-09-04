from rest_framework import viewsets

from .models import Domain
from .serializers import DomainSerializer

# Create your views here.
class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
