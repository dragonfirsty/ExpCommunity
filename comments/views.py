from django.shortcuts import get_object_or_404
from posts.models import Post
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Comment
from .permissions import AbleToComment,IsOwnerOrAdmin
from .serializers import CommentCreateSerializer, CommentSerializer
from .utils.mixins import SerializerByMethodMixin


class CommentView(SerializerByMethodMixin, ListCreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,AbleToComment]
    lookup_field = "post_id"
    queryset = Comment.objects.all()
    serializer_map = {
        "GET": CommentSerializer,
        "POST": CommentCreateSerializer,
    }

    def perform_create(self, serializer):

        post_id = get_object_or_404(Post, pk=self.kwargs.get("post_id"))

        serializer.save(user=self.request.user, post=post_id)


class CommentDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsOwnerOrAdmin]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
