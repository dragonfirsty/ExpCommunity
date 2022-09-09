from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Comment
from .permissions import CommentPermissions
from .serializers import CommentCreateSerializer, CommentSerializer
from .utils.mixins import SerializerByMethodMixin


class CommentView(SerializerByMethodMixin, ListCreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [CommentPermissions]

    queryset = Comment.objects.all()
    serializer_map = {
        "GET": CommentSerializer,
        "POST": CommentCreateSerializer,
    }

    def perform_create(self, serializer):

        serializer.save(user=self.request.user, post=self.request.post)


class CommentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

