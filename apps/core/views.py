from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.core.models import Group, Events
from apps.user.permissions import RoleBasedAPIPermission
from apps.core.serializers import GroupSerializers, EventSerializers


class GroupViewSet(ModelViewSet):
    start_name = 'groups'
    queryset = Group.objects.all()
    serializer_class = GroupSerializers
    permission_classes = [IsAuthenticated, RoleBasedAPIPermission]


class EventViewSet(ModelViewSet):
    start_name = 'events'
    queryset = Events.objects.all()
    serializer_class = EventSerializers
    permission_classes = [IsAuthenticated, RoleBasedAPIPermission]
