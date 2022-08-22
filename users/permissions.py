from rest_framework import permissions
from rest_framework.views import Request, View

class IsAdminOrCritic(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:

        return request.user.is_superuser or request.user.is_critic and request.user.id == view.kwargs['user_id']