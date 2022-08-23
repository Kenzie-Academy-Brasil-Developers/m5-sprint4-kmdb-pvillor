from rest_framework import permissions
from rest_framework.views import Request, View

from reviews.models import Review

class IsAdminOrCriticOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:

        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_superuser or request.user.is_critic

    def has_object_permission(self, request: Request, view: View, review: Review):
        return request.user.is_superuser or request.user == review.critic