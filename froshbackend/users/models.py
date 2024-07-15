from django.db import models
from django.test import TestCase
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .managers import CustomUserManager
from .utils import generate_user_secure_id, qr_maker
import logging
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import random
import string
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import CustomUserManager
from django.conf import settings
import os
from .utils import qr_maker

def default_events():
    return []
logger = logging.getLogger(__name__)
class User(AbstractUser):
    username = None
    password=models.CharField(blank=True)
    image = models.URLField(blank=True)
    registration_id = models.CharField(unique=True, max_length=20)

    secure_id = models.CharField(unique=True, max_length=8, null=True, blank=True)
    events = ArrayField(base_field=models.CharField(max_length=60), max_length=50, blank=True, default=list)
    qr = models.URLField(blank=True)
    last_scanned = models.DateTimeField(auto_now=True, blank=True)
    is_scanned = models.BooleanField(default=False)


    USERNAME_FIELD = "registration_id"
    REQUIRED_FIELDS = ['image', 'qr']
    objects = CustomUserManager()


    
    def save(self, *args, **kwargs):
        is_new = self._state.adding
        logger.info(f"Saving user {self.registration_id}, is_new: {is_new}")

        if is_new and not self.secure_id:
            
            self.secure_id = generate_user_secure_id()
            logger.info(f"Generated secure_id in save method: {self.secure_id}")

        super().save(*args, **kwargs)

        if is_new and not self.qr:
            logger.info(f"Generating QR code for new user {self.registration_id}")
            self.generate_qr_code()

    def generate_qr_code(self):
        try:
            qr_value = f"{self.registration_id}"
            logger.info(f"Creating QR code with value: {qr_value}")
            qr_file_path = qr_maker(qr_value, self.registration_id)
            logger.info(f"QR code created at: {qr_file_path}")
            
            relative_path = os.path.join('qr_codes', os.path.basename(qr_file_path))
            full_path = os.path.join(settings.MEDIA_ROOT, relative_path)
            
            logger.info(f"Creating directory: {os.path.dirname(full_path)}")
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            
            logger.info(f"Moving file from {qr_file_path} to {full_path}")
            os.rename(qr_file_path, full_path)
            
            self.qr = os.path.join(settings.MEDIA_URL, relative_path)
            logger.info(f"Saving user with QR URL: {self.qr}")
            super().save(update_fields=['qr'])
        except Exception as e:
            logger.error(f"Error generating QR code: {str(e)}")
            raise

@receiver(pre_save, sender=User)
def user_pre_save(sender, instance, **kwargs):
    logger.info(f"Pre-save signal for user {instance.registration_id}")

@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, **kwargs):
    logger.info(f"Post-save signal for user {instance.registration_id}, created: {created}")

@receiver(pre_save, sender=User)
def ensure_secure_id(sender, instance, **kwargs):
    if not instance.secure_id:
        instance.secure_id = generate_user_secure_id()
        logger.info(f"Generated secure_id in pre_save signal: {instance.secure_id}")