from rest_framework import serializers
from .models import Answer

from user.serializers import UserSerializer
from comments.serializers import CommentImportSerializer

class AnswerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    comment = CommentImportSerializer(read_only=True)
    class Meta:
        model = Answer
        fields = "__all__"
        extra_kwargs = {
            "created_at": {"read_only": True},
            "uuid": {"read_only": True},
            "updated_at": {"read_only": True},
        }


class AnswerCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    comment = CommentImportSerializer(read_only=True) 

    class Meta:
        model = Answer
        fields = ["uuid","description", "user", "comment"]
        extra_kwargs = {
            "uuid": {"read_only": True}
        }
        