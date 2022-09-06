from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.generics import DestroyAPIView, ListCreateAPIView, UpdateAPIView
from .utils.mixins import SerializerByMethodMixin
from .models import Comment
from .permissions import CommentPermissions
from .serializers import CommentSerializer,CommentCreateSerializer


class CommentView(SerializerByMethodMixin,ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CommentPermissions]

    queryset = Comment.objects.all()
    serializer_map = {
        "GET": CommentSerializer,
        "POST": CommentCreateSerializer,
    }
    
    def perform_create(self, serializer):
        
        serializer.save(user = self.request.user,post = self.request.post)

class CommentDeleteView(DestroyAPIView):
    ...

class CommentUpdateView(UpdateAPIView):
    ...