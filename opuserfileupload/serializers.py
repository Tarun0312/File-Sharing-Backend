from rest_framework import serializers
from .models import OperationUser

class OperartionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OperationUser
        fields ="__all__"
        