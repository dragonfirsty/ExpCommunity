from rest_framework import serializers

from user.serializers import UserSerializer

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    user_id = UserSerializer(read_only=True)["uuid"]

    class Meta:
        model = Post
        fields = [
            "uuid",
            "description",
            "media",
            "user_id",
        ]
        read_only_fields = ["uuid", "user_id"]
