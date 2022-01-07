#  Django Rest Framework
from rest_framework import fields, serializers

from questions.models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'