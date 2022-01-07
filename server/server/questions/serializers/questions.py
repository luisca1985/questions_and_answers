#  Django Rest Framework
from rest_framework import serializers

from server.questions.models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'