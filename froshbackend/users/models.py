from django.db import models
from django.test import TestCase
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .manager import CustomUserManager
class User(AbstractUser):
    username = None
    image = models.URLField()
    registration_id = models.CharField(unique=True, max_length=20)
    secure_id = models.CharField(unique=True, max_length=8, null=True, blank=True)
    events = ArrayField(base_field=models.CharField(max_length=60), max_length=50, blank=True, default=list)
    qr = models.URLField(blank=True)
    USERNAME_FIELD = "registration_id"
    REQUIRED_FIELD = ['image', 'qr']
    objects = CustomUserManager()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"