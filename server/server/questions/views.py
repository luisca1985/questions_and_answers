# Django Rest Framework
from rest_framework import serializers, viewsets, status
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
        serializer = QuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None): # /api/questions/<str:id>
        question = Question.objects.get(id=pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def update(self, request, pk=None): # /api/questions/<str:id>
        question = Question.objects.get(id=pk)
        serializer = QuestionSerializer(instance=question, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None): # /api/questions/<str:id>
        question = Question.objects.get(id=pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)