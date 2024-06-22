from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

class User(AbstractUser):

    username = None
    image = models.URLField()
    registration_id = models.CharField(unique=True, max_length=20)
    secure_id = models.CharField(unique=True, max_length=8, null=True, blank=True)
    events = ArrayField(base_field=models.CharField(max_length=60), max_length=50, blank=True, default=list)
    qr = models.URLField(blank=True)
    hood = models.ForeignKey(Hood, on_delete=models.DO_NOTHING, blank=True, null=True)
    hood_points = models.IntegerField(default=0)

    USERNAME_FIELD = "registration_id"
    REQUIRED_FILEDS = ['image', 'qr']
    objects = UserManager()
    is_scanned = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


    