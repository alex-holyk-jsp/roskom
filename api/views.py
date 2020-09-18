from rest_framework import viewsets, permissions
from rest_framework.response import Response

from .models import Domain
from .serializers import BaseDomainSerializer, AnonymousUserDomainSerializer
from .helpers import get_client_ip, send_email


STATUS_APPROVED = 'approved'


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

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        old_status = instance.status
        new_status = request.data.get('status')

        if old_status != STATUS_APPROVED and new_status == STATUS_APPROVED:
            send_email(instance.owner_email)

        instance.status = new_status
        instance.save()

        self.perform_update(serializer)
        return Response(serializer.data)
