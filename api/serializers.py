from rest_framework import serializers
from .models import Domain


class DomainSerializer(serializers.ModelSerializer):
    owner_ip = serializers.ReadOnlyField()
    status = serializers.CharField()

    class Meta:
        model = Domain
        fields = ['id', 'domain', 'ip', 'owner_ip', 'status']