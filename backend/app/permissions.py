from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """
    Custom permission to only allow admins to access the view.
    """

    def has_permission(self, request, view):
        return request.user and request.user.role == "admin"


class IsStaff(permissions.BasePermission):
    """
    Custom permission to only allow staff to access the view.
    """

    def has_permission(self, request, view):
        return request.user and request.user.role == "staff"


class IsAdminOrStaff(permissions.BasePermission):
    """
    Custom permission to allow both admin and staff to access the view.
    """

    def has_permission(self, request, view):
        return request.user and request.user.role in ["admin", "staff"]
