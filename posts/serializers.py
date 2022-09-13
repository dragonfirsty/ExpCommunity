from rest_framework import serializers

from user.serializers import UserSerializer
from groups.serializers import GroupSerializer
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ["uuid", "user", "group"]
