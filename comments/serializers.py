from rest_framework import serializers

from .models import Comment
from user.serializers import UserSerializer
from posts.serializers import PostSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        extra_kwargs = {
            "created_at": {"read_only": True},
            "id": {"read_only": True},
            "updated_at": {"read_only": True},
        }


class CommentCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    post = PostSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["description", "user", "post"]
