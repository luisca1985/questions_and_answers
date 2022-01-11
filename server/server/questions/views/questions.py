# Django Rest Framework
from rest_framework import  viewsets

# Models
from server.questions.models import Question

# Filters
from rest_framework.filters import SearchFilter

# Serializers
from server.questions.serializers import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # Filters
    filter_backends = [SearchFilter]
    search_fields = ['title', 'detail']