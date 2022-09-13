from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Answer
from groups.models import Group

class AbleToAnswer(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:

        if request.method == "GET":
            return True

        geral_group = Group.objects.get(name='geral')

        if geral_group.user_id == request.user.id:
            return False

        group = Group.objects.get(id=view.kwargs['group_id'])

        return request.user.id == group.user_id

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request: Request, view: View, answer: Answer):

        return answer.user_id == request.user.id