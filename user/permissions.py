from .models import users
from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False

class IsMember(permissions.BasePermission):
    def has_permission(self, request):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False
