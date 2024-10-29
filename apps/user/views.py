from rest_framework import generics
from .models import Role
from rest_framework.permissions import IsAuthenticated
from .permissions import RoleBasedAPIPermission
from .serializers import RolePermissionSerializer


class RoleCreateView(generics.CreateAPIView):
    start_name = 'rolepermission'
    queryset = Role.objects.all()
    serializer_class = RolePermissionSerializer
    permission_classes = [IsAuthenticated, RoleBasedAPIPermission]


class RoleRetrieveView(generics.RetrieveUpdateAPIView):
    start_name = 'rolepermission'
    queryset = Role.objects.all()
    serializer_class = RolePermissionSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, RoleBasedAPIPermission]
