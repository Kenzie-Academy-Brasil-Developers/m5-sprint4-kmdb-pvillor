from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    birthdate = models.DateField()
    bio = models.TextField(null=True, blank=True)
    is_critic = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ["email", "first_name", "last_name", "birthdate"]