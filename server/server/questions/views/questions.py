# Django Rest Framework
from rest_framework import viewsets, status, generics
from rest_framework.response import Response

# Models
from server.questions.models import Question

# Filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# Serializers
from server.questions.serializers import QuestionSerializer


# class QuestionViewSet(viewsets.ViewSet):
# class QuestionViewSet(viewsets.ModelViewSet):
class QuestionViewSet(viewsets.ModelViewSet):


    # Filters
    # queryset = Question.objects.all()
    # serializer_class = QuestionSerializer
    # filter_backends = (SearchFilter)
    # search_fields = ['title', 'detail']

    def list(self, request):  # /api/questions
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):  # /api/questions
        serializer = QuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None): # /api/questions/<str:id>
        question = Question.objects.get(id=pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data, status=status.HTTP_200_OK)

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

    # def filter_queryset(self, queryset):
    #     filter_backends = (DjangoFilterBackend, )
        
    #     # Other condition for different filter backend goes here
    #     for backend in list(filter_backends):
    #         queryset = backend().filter_queryset(self.request, queryset, view=self)
    #     return queryset
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Question.objects.all()
        title = self.request.query_params.get('title')
        if title is not None:
            queryset = queryset.filter(question__title=title)
        return queryset