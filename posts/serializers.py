from rest_framework import serializers

from user.serializers import UserSerializer

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    user_id = UserSerializer(read_only=True)["id"]

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ["uuid", "user_id", "group_id"]
