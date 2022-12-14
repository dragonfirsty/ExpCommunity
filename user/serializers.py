from groups.models import Group
from groups.serializers import GroupCreateSerializer
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    groups = GroupCreateSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = [
            "uuid",
            "username",
            "email",
            "first_name",
            "last_name",
            "birthdate",
            "post_permission",
            "password",
            "groups",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "uuid": {"read_only": True},
        }

    def create(self, validated_data) -> User:
        groups_data = None
        if validated_data.get("groups"):
            groups_data = validated_data.pop("groups")

        user = User.objects.create_user(**validated_data)

        if groups_data:
            for value in groups_data:
                group, _ = Group.objects.get_or_create(**value)
                user.groups.add(group)

        return user

    def update(self, instance, validated_data):
        groups_data = None
        if validated_data.get("groups"):
            groups_data = validated_data.pop("groups")

        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        if groups_data:
            for value in groups_data:
                group, _ = Group.objects.get_or_create(**value)
                instance.groups.add(group)

        instance.save()

        return instance


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)


