from rest_framework import serializers
from .models import Role, APIAction


class RolePermissionSerializer(serializers.ModelSerializer):
    api_actions = serializers.PrimaryKeyRelatedField(
        queryset=APIAction.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = Role
        fields = ['id', 'role', 'api_actions']
