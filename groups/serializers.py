from rest_framework import serializers
from user.serializers import UserSerializer

from .models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class GroupCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Group
        fields = ["name", "user"]
