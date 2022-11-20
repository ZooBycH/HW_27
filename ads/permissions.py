from rest_framework.permissions import BasePermission

from users.models import UserRole


class IsOwnerSelection(BasePermission):
    message = "Вы не являетесь владельцем данной подборки"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False


class IsOwnerAdOrStaff(BasePermission):
    message = "Вы не являетесь владельцем объявления или администратором"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author or request.user.role in [UserRole.ADMIN, UserRole.MODERATOR]:
            return True
        return False

