"""Answer model."""

# Django
from django.db import models

# Utilities
from server.utils.models import QAModel

# Questions
from .questions import Question


class Answer(QAModel):
    """Answer model.

    Answer made for a user.
    """
    # question = Question
    detail = models.CharField(
        'Answer detail',
        default='detail', 
        max_length=500
    )
    is_correct =  models.BooleanField(
        'this is the correct answer',
        default=False,
        help_text='This is the correct answer select by the user who asked the question.'
    )

    # def __str__(self):
    # """Returns question's str representation"""
    # return str(self.title)

    class Meta(QAModel.Meta):
        """Meta class"""

        ordering = ['-is_correct', '-modified', '-created']