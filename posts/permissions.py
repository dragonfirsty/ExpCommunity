from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Post



class AbleToPost(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        user = request.user
        group_id = view.kwargs.get('group_id')
        if user.is_superuser and request.method == "GET":
            return True
        if user.is_superuser and request.user.post_permission:
            return True
        group_atual =user.groups.get(uuid=group_id)

        if group_atual and request.method == "GET":
            return True

        if group_atual.name != 'geral' and user.post_permission:
            return True
        return False
class IsOwnerOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request: Request, view: View, post: Post):

        return post.user_id == request.user.uuid or request.user.is_superuser