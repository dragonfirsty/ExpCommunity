from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Post
from groups.models import Group


class AbleToPost(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:

        if request.method == "GET":
            return True

        geral_group = Group.objects.get(name='geral')

        if geral_group.user_id == request.user.uuid:
            return request.user.is_superuser

        group = Group.objects.get(uuid=view.kwargs['group_id'])

        return request.user.uuid == group.user_id and request.user.post_permission

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request: Request, view: View, post: Post):

        return post.user_id == request.user.id