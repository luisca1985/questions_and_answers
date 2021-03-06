"""User models admin."""

# Django
from django.contrib import admin

# Models

from server.questions.models import Question, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Question model admin."""

    list_display = ('asked_by', 'title', 'detail', 'answers_made',
                    'is_resolved', 'is_closed', 'is_public')
    search_fields = ('asked_by__username', 'asked_by__email')
    list_filter = ('asked_by__username', 'asked_by__email',
                   'is_resolved', 'is_closed', 'is_public', 'created', 'modified')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    """Answer model admin."""

    list_display = ('question_to_answer', 'answered_by',
                    'detail', 'is_correct')
    search_fields = ('question_to_answer__title',
                     'answered_by__username', 'answered_by__email')
    list_filter = ('question_to_answer__title', 'answered_by__username',
                   'answered_by__email', 'is_correct', 'created', 'modified')
