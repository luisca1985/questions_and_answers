from django.contrib import admin
from django.urls import path

from server.questions.views import QuestionViewSet

urlpatterns = [
    path('questions', QuestionViewSet.as_view({
        'get':'list',
        'post':'create',

    })),
    path('questions/<str:pk>', QuestionViewSet.as_view({
        'get':'retrieve',
        'delete':'destroy',
        
    }))
]
