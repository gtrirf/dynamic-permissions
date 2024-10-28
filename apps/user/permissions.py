from rest_framework.permissions import BasePermission


class RoleBasedAPIPermission(BasePermission):
    def has_permission(self, request, view):
        role = getattr(request.user, 'role', None)
        if not role:
            return False

        api_name = getattr(view, 'start_name', None).lower()
        action = getattr(view, 'action', None)

        if action is None:
            return False

        allowed_actions = role.api_actions.filter(api=api_name, action=action)
        return allowed_actions.exists()
