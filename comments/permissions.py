from rest_framework import permissions


class CommentPermissions(permissions.BasePermission):
    def has_object_permission(self, request, _, obj):

        return (
            request.user.is_authenticated
            and (request.method in permissions.SAFE_METHODS
            or request.user.group.id == obj.post.group.id)
        )