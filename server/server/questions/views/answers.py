# Django Rest Framework
from rest_framework import viewsets, status
from rest_framework.response import Response

# Models
from server.questions.models import Answer

# Serializers
from server.questions.serializers import AnswerSerializer


class AnswerViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/answers
        answers = Answer.objects.all()
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)


    def list_for_question(self, request, pk=None):  # /api/questions/<str:id>/answers
        answers = Answer.objects.filter(question_to_answer=pk)
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)


    def create(self, request):  # /api/answers
        serializer = AnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None): # /api/answers/<str:id>
        answer = Answer.objects.get(id=pk)
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)

    def update(self, request, pk=None): # /api/answers/<str:id>
        answer = Answer.objects.get(id=pk)
        serializer = AnswerSerializer(instance=answer, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None): # /api/answers/<str:id>
        answer = Answer.objects.get(id=pk)
        answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)