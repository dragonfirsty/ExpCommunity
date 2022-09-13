from comments.models import Comment
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Answer
from .permissions import AbleToAnswer, IsOwner
from .serializers import AnswerCreateSerializer, AnswerSerializer
from .utils.mixins import SerializerByMethodMixin


class AnswerView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Answer.objects.all()
    serializer_map = {
        "GET": AnswerSerializer,
        "POST": AnswerCreateSerializer,
    }
    lookup_field = "comment_id"

    def perform_create(self, serializer):

        comment_id = get_object_or_404(Comment, pk=self.kwargs.get("comment_id"))

        serializer.save(user=self.request.user, comment=comment_id)


class AnswerDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
