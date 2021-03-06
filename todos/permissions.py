from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Extends BasePermission
    """

    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only alloewd to the author of a post
        return obj.author == request.user


class IsAuthor(permissions.BasePermission):
    """
    Only author of task can perform actions
    """

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user