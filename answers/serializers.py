from rest_framework import serializers
from .models import Answer

class AnswerSerializer(serializers.ModelSerializer):
    model = Answer
    fields = '__all__'
    read_only_fields = ['user_id', 'comment_id']