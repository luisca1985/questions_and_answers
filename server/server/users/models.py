"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utilities
from server.utils.models import QAModel

# Create your models here.


class Users(QAModel, AbstractUser):
    """User model.

    Extend from Django's Abstract User, change the username field
    to email and add some extra fields.
    """
    email = models.EmailField(
        'email_address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists'
        }

        USERNAME_FIELD='email'
        REQUIRED_FIELDS=['username', 'first_name', 'last_name']

        def __str__(self):
        """Return username"""
        return self.username

        def get_short_name(self):
        """Return username"""
        return self.username

    )
