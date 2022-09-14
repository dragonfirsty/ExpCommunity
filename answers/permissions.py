from rest_framework import permissions
from rest_framework.views import Request, View
from comments.models import Comment
from posts.models import Post
from .models import Answer

class AbleToAnswer(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        user = request.user
        if user.is_superuser and request.method == "GET":
            return True
        if user.is_superuser and request.user.post_permission:
            return True
        comment_id = view.kwargs.get("comment_id")
        post_id = Comment.objects.get(uuid=comment_id).post_id
        group_id = Post.objects.get(uuid=post_id).group_id
    
        group_atual = user.groups.get(uuid=group_id)
        if group_atual and request.method == "GET":
            return True

        if group_atual.name != "geral" and user.post_permission:
            return True
        return False


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, answer: Answer):

        return answer.user_id == request.user.uuid or request.user.is_superuser
