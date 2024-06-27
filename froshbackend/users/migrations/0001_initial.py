import json
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None
    image = models.URLField()
    registration_id = models.CharField(unique=True, max_length=20)
    is_scanned = models.DateTimeField()
    secure_id = models.CharField(unique=True, max_length=8, null=True, blank=True)
    events = models.TextField(blank=True, default='[]')  # Store as JSON string
    qr = models.URLField(blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    USERNAME_FIELD = 'registration_id'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def set_events(self, events_list):
        self.events = json.dumps(events_list)

    def get_events(self):
        return json.loads(self.events)