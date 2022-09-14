from rest_framework import permissions
from rest_framework.views import Request, View
from posts.models import Post
from .models import Comment

class AbleToComment(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        user = request.user
        if user.is_superuser and request.method == "GET":
            return True
        if user.is_superuser and request.user.post_permission:
            return True
        post_id = view.kwargs.get("post_id")
        group_id = Post.objects.get(uuid=post_id).group_id
    
        group_atual = user.groups.get(uuid=group_id)
        if group_atual and request.method == "GET":
            return True

        if group_atual.name != "geral" and user.post_permission:
            return True
        return False


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, comment: Comment):

        return comment.user_id == request.user.uuid or request.user.is_superuser
