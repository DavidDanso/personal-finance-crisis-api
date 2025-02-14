from django.shortcuts import render
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

# Authentication Models
class User(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
