from django.shortcuts import get_object_or_404
from groups.models import Group
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Post
from .permissions import AbleToPost, IsOwner
from .serializers import PostSerializer


class PostView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "group_id"

    def perform_create(self, serializer):

        group_id = get_object_or_404(Group, pk=self.kwargs.get("group_id"))

        serializer.save(user=self.request.user, group=group_id)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Post.objects.all()
    serializer_class = PostSerializer
