from django.contrib import admin
from django.urls import path

from server.questions.views import QuestionViewSet, AnswerViewSet


urlpatterns = [
    path('questions/<str:pk>', QuestionViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy',
        
    })),
    path('questions', QuestionViewSet.as_view({
        'get':'list',
        'post':'create',

    })),
    path('answers/<str:pk>', AnswerViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy',
        
    })),
    path('answers', AnswerViewSet.as_view({
        'get':'list',
        'post':'create',

    }))
]
