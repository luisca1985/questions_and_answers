"""User models admin."""

# Django
from django.contrib import admin

# Models

from server.questions.models import Question, Answer



@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Question model admin."""

    list_display = ('created_by','title','detail', 'answers_made', 'is_resolved', 'is_closed', 'is_public')
    search_fields = ('created_by__username','created_by__email')
    list_filter = ('created_by__username','created_by__email','is_resolved', 'is_closed', 'is_public', 'created', 'modified')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    """Answer model admin."""

    list_display = ('detail', 'is_correct' )
    # search_fields = ('question__title',)
    list_filter = (
        # 'question__title',
        'is_correct',
        )