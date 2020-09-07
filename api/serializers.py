from rest_framework import serializers
from .models import Domain


class BaseDomainSerializer(serializers.ModelSerializer):
    owner_ip = serializers.ReadOnlyField()

    class Meta:
        model = Domain
        fields = ['id', 'domain', 'ip', 'owner_ip', 'status']


class AnonymousUserDomainSerializer(BaseDomainSerializer):
    status = serializers.ReadOnlyField()
