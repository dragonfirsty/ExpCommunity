from rest_framework import permissions
from rest_framework.views import Request,View
from .models import User


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request:Request, view:View) -> bool:
        
        return request.user.is_superuser


class IsOwnerOrAdmin(permissions.BasePermission):
    
    def has_object_permission(self, request:Request, view:View, user: User):

        if request.method == "PATCH" or request.method == "DELETE":
            return request.user.is_superuser

        
        return user == request.user or request.user.is_superuser



