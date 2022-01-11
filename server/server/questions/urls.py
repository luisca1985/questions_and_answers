from django.contrib import admin
from django.urls import path
from django.urls.conf import include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from server.questions.views import QuestionViewSet, AnswerViewSet

router = DefaultRouter()

router.register(r'questions', QuestionViewSet,basename='question')
router.register(r'answers', AnswerViewSet,basename='answer')

urlpatterns = [
    path('questions/<str:pk>/answers', AnswerViewSet.as_view({'get':'list_for_question',})),
    path('', include(router.urls))
]