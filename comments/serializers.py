from rest_framework import serializers

from .models import Comment

from user.serializers import UserSerializer
from posts.serializers import PostImportSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    post = PostImportSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = "__all__"
        extra_kwargs = {
            "created_at": {"read_only": True},
            "uuid": {"read_only": True},
            "updated_at": {"read_only": True},
        }


class CommentCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    post = PostImportSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["uuid","description", "user", "post"]
        extra_kwargs = {
            "uuid": {"read_only": True}
        }

class CommentImportSerializer(serializers.ModelSerializer):
     class Meta:
        model = Comment
        fields = [
            "uuid",
            "description"
        ]
        read_only_fields = ["uuid"] 