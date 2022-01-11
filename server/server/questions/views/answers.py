# Django Rest Framework
from rest_framework import viewsets
from rest_framework.response import Response

# Models
from server.questions.models import Answer

# Serializers
from server.questions.serializers import AnswerSerializer
from server.questions.permissions import AnswerPermission


class AnswerViewSet(viewsets.ModelViewSet):

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (AnswerPermission,)

    def list_for_question(self, request, pk=None):  # /api/questions/<str:id>/answers
        answers = Answer.objects.filter(question_to_answer=pk)
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)