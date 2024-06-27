from django.db import models
from django.test import TestCase
from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import pre_save
from django.dispatch import receiver
from .manager import CustomUserManager
def default_events():
    return []

class User(AbstractUser):
    username = None
    image = models.URLField()
    registration_id = models.CharField(unique=True, max_length=20)
    secure_id = models.CharField(unique=True, max_length=8, null=True, blank=True)
    qr = models.URLField(blank=True)
    # events = models.JSONField(default=default_events, blank=True) 
    USERNAME_FIELD = "registration_id"
    REQUIRED_FIELD = ['image', 'qr']
    objects = CustomUserManager()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"