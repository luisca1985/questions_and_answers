"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser 

# Utilities
from server.utils.models import QAModel

# Create your models here.

class Users(QAModel, AbstractUser):
    pass