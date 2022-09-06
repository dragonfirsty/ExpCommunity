from dataclasses import field
from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username','email',"first_name","last_name",'birthdate','post_permission',"is_superuser","password"]
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)