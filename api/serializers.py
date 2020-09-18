from rest_framework import serializers
from .models import Domain


class BaseDomainSerializer(serializers.ModelSerializer):
    owner_ip = serializers.ReadOnlyField()
    owner_email = serializers.ReadOnlyField()

    class Meta:
        model = Domain
        fields = ['id', 'domain', 'ip', 'owner_ip', 'status', 'owner_email']


class AnonymousUserDomainSerializer(BaseDomainSerializer):
    status = serializers.ReadOnlyField()
    owner_email = serializers.EmailField(max_length=200)

