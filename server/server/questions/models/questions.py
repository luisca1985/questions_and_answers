"""Question model."""

# Django
from django.db import models

# Utilities
from server.utils.models import QAModel


class Question(QAModel):
    """Question model.

    Questions asked for user.
    """

    created_by = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        help_text='User who has created the question',
        related_name='created_by',
        null=True
    )

    title = models.CharField(
        'question title',
        default='title', 
        max_length=140
    )
    # slug_name = models.SlugField(unique=True, max_length=40)
    detail = models.CharField(
        'Question detail',
        default='detail', 
        max_length=500
    )
    answers_made = models.PositiveIntegerField(default=0)
    is_resolved =  models.BooleanField(
        'resolved question',
        default=False,
        help_text='The question has been resolved by other user.'
    )
    is_closed =  models.BooleanField(
        'closed question',
        default=False,
        help_text='The question has been closed by the user.'
    )
    is_public =  models.BooleanField(
        'public question',
        default=True,
        help_text='The question has been hidden.'
    )

    def __str__(self):
        """Returns question's str representation"""
        return str(self.title)
