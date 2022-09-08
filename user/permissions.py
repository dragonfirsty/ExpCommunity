from rest_framework import permissions
from rest_framework.views import Request,View


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request:Request, view:View) -> bool:
        
        if request.method == "POST":
            return True
        
        return request.user.is_superuser