from rest_framework import serializers

from user.serializers import UserSerializer
from groups.serializers import GroupSerializer
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    user_id = UserSerializer(read_only=True)["uuid"]
    group_id = GroupSerializer(read_only=True)["uuid"]
    class Meta:
        model = Post
        fields = '__all__'
        lookup_field = 'group_id_id'
        read_only_fields = ["uuid", "user_id", "group_id"]
