# Django Rest Framework
from rest_framework import viewsets
from rest_framework.response import Response

# Models
from server.questions.models import Question

# Serializers
from server.questions.serializers import QuestionSerializer


class QuestionViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/questions
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def create(self, request):  # /api/questions
        pass

    def retrieve(self, request, pk=None): # /api/questions/<str:id>
        pass

    def update(self, request, pk=None): # /api/questions/<str:id>
        pass

    def destroy(self, request, pk=None): # /api/questions/<str:id>
        pass