"""Profile model."""

# Django
from django.db import models
from django.db.models.deletion import CASCADE

# utilities
from server.utils.models import QAModel

class Profile(QAModel):
    """Profile model.
    
    A profile holds a user's public data.
    """

    users = models.OneToOneField('users.User', on_delete=models.CASCADE)

    questions_asked = models.PositiveIntegerField(default=0)
    answers_made = models.PositiveIntegerField(default=0)
    reputation = models.FloatField(
        default=0.5,
        help_text="User's reputation based on questions and answers."
    )

    def __str__(self):
        """Returns user's str representation"""
        return str(self.user)