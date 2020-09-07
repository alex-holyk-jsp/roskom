from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from .models import Domain
from .serializers import DomainSerializer
from .helpers import get_client_ip

# Create your views here.
class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer

    def perform_create(self, serializer):
        client_ip = get_client_ip(self.request)
        serializer.save(owner_ip=client_ip)

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def update(self, request, *args, **kwargs):
        print('>>>> update')
        pass

    def partial_update(self, request, *args, **kwargs):
        print('>>>> partial_update')
        pass
