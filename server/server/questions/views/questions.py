# Django Rest Framework
from rest_framework import  viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Models
from server.questions.models import Question

# Filters
from rest_framework.filters import SearchFilter

# Serializers
from server.questions.serializers import QuestionSerializer

# Permission
from server.questions.permissions import QuestionPermission


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # Filters
    filter_backends = [SearchFilter]
    search_fields = ['title', 'detail']
    # Permissions
    permission_classes = (QuestionPermission,)