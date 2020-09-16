from rest_framework import viewsets, permissions

from .models import Domain
from .serializers import BaseDomainSerializer, AnonymousUserDomainSerializer
from .helpers import get_client_ip

# Create your views here.
class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()

    def perform_create(self, serializer):
        client_ip = get_client_ip(self.request)
        serializer.save(owner_ip=client_ip)

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return BaseDomainSerializer
        return AnonymousUserDomainSerializer
