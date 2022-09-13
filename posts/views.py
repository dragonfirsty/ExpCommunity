from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Post
from groups.models import Group
from .serializers import PostSerializer
from .permissions import AbleToPost, IsOwner

class PostView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'group_id'
    def perform_create(self, serializer):
        
        serializer.save(user_id = self.request.user)
    


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 

    queryset = Post.objects.all()
    serializer_class = PostSerializer