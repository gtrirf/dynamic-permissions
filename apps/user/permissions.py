from rest_framework.permissions import BasePermission
from .tools import ACTIONS


class RoleBasedAPIPermission(BasePermission):
    def has_permission(self, request, view):
        role = getattr(request.user, 'role', None)
        if not role:
            return False

        api_name = getattr(view, 'start_name', None)
        action = ACTIONS.get(request.method)
        if not api_name or not action:
            return False

        if action is None:
            return False

        if isinstance(action, list):
            return any(role.api_actions.filter(api=api_name.lower(), action=act).exists() for act in action)
        else:
            return role.api_actions.filter(api=api_name.lower(), action=action).exists()
