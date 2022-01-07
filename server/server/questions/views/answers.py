# Django Rest Framework
from rest_framework import viewsets, status
from rest_framework.response import Response

# Models
from server.questions.models import Answer

# Serializers
from server.questions.serializers import AnswerSerializer


class AnswerViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/answers
        questions = Answer.objects.all()
        serializer = AnswerSerializer(questions, many=True)
        return Response(serializer.data)

    def create(self, request):  # /api/questions
        serializer = AnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None): # /api/questions/<str:id>
        question = Answer.objects.get(id=pk)
        serializer = AnswerSerializer(question)
        return Response(serializer.data)

    def update(self, request, pk=None): # /api/questions/<str:id>
        question = Answer.objects.get(id=pk)
        serializer = AnswerSerializer(instance=question, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None): # /api/questions/<str:id>
        question = Answer.objects.get(id=pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)