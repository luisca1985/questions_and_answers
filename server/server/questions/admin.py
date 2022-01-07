"""User models admin."""

# Django
from django.contrib import admin

# Models

from server.questions.models import Question, Answer



@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Question model admin."""

    list_display = ('title','detail', 'answers_made', 'is_resolved', 'is_closed', 'is_public' )
    list_filter = ('is_resolved', 'is_closed', 'is_public', 'created', 'modified')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    """Answer model admin."""

    list_display = ('detail', 'is_correct' )
    # search_fields = ('question__title',)
    list_filter = (
        # 'question__title',
        'is_correct',
        )