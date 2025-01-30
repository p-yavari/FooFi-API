from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Grants permission if the user is accessing their own profile."""

        return obj.pk == request.user.pk


class UpdateOwnStatus(permissions.BasePermission):
    """Allows users to update their own tasks"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own task"""

        return obj.user_profile.pk == request.user.pk
