from django.contrib.auth.models import AbstractUser
from django.db import models

"""
UserProfile Model
"""


class UserProfile(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.username
