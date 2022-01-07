#  Django Rest Framework
from rest_framework import serializers

from server.questions.models import Answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'