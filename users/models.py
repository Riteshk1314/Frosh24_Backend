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
from django.core.mail import send_mail
from .utils import send_credentials_email
from hoods.models import Hoods
def default_events():
    return []
logger = logging.getLogger(__name__)
def generate_random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12))


logger = logging.getLogger(__name__)

class User(AbstractUser):
    username = None
    # In the provided code snippet, `name=models` seems to be a mistake or an incomplete definition.
    # It should be corrected to define the `name` field properly in the `User` model.
    name=models.CharField(blank=True, max_length=128)
    password = models.CharField(blank=True, max_length=128)
    image = models.URLField(blank=True)
    registration_id = models.CharField(unique=True, max_length=20)
    secure_id = models.CharField( primary_key=True, blank=True)
    events = ArrayField(base_field=models.CharField(max_length=60), max_length=50, blank=True, default=list)
    email=models.EmailField()
    # qr = models.URLField(blank=True)
    # last_scanned = models.DateTimeField(auto_now=True, blank=True)
    # is_scanned = models.BooleanField(default=False)
    # is_booked = models.BooleanField(default=False)
    # qr_code_image=models.URLField(blank=True)
    USERNAME_FIELD = "registration_id"
    # REQUIRED_FIELDS = ['image', 'qr']
    objects = CustomUserManager()
    hood_name = models.ForeignKey(
        Hoods,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='users'
    )

    # def generate_qr_code(self):
    #     try:
    #         qr_value = f"{self.registration_id}"
    #         logger.info(f"Creating QR code with value: {qr_value}")
    #         qr_file_path = qr_maker(qr_value, self.registration_id)
    #         logger.info(f"QR code created at: {qr_file_path}")
            
    #         relative_path = os.path.join('qr_codes', os.path.basename(qr_file_path))
    #         full_path = os.path.join(settings.MEDIA_ROOT, relative_path)
            
    #         logger.info(f"Creating directory: {os.path.dirname(full_path)}")
    #         os.makedirs(os.path.dirname(full_path), exist_ok=True)
            
    #         logger.info(f"Moving file from {qr_file_path} to {full_path}")
    #         os.rename(qr_file_path, full_path)
            
    #         return os.path.join(settings.MEDIA_URL, relative_path)
    #     except Exception as e:
    #         logger.error(f"Error generating QR code: {str(e)}")
    #         raise

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        update_fields = kwargs.get('update_fields', None)

        if is_new:
            if not self.secure_id:
                self.secure_id = generate_user_secure_id()
            
            # raw_password = None
            # if not self.password:
            #     raw_password = generate_random_password()
            #     print(raw_password)
            #     self.set_password(raw_password)

            # if not self.qr:
            #     self.qr = self.generate_qr_code()
            kwargs.pop('update_fields', None)
        elif update_fields is not None:
  
            kwargs['update_fields'] = update_fields

        super().save(*args, **kwargs)

# mailing is commented for the purpose of setting up db 
        if is_new and raw_password:
            send_credentials_email(self.email, self.registration_id, raw_password)
            
             
            
            
            
# @receiver(pre_save, sender=User)
# def user_pre_save(sender, instance, **kwargs):
#     logger.info(f"Pre-save signal for user {instance.registration_id}")
    
    
        
#     raw_password = generate_random_password()
#     instance.set_password(raw_password)
#     send_credentials_email(instance.email, instance.registration_id, raw_password)
#     logger.info(f"Generated and set random password for user {instance.registration_id}")

# @receiver(post_save, sender=User)
# def user_post_save(sender, instance, created, **kwargs):
#     logger.info(f"Post-save signal for user {instance.registration_id}, created: {created}")
    
#     if created and not instance.qr:
#         logger.info(f"Generating QR code for new user {instance.registration_id}")
#         instance.generate_qr_code()
#     if instance._state.adding:
#             if not instance.secure_id:
#                 instance.secure_id = generate_user_secure_id()
#                 logger.info(f"Generated secure_id in pre_save signal: {instance.secure_id}")
                
#     raw_password = generate_random_password()
#     instance.set_password(raw_password)
#     send_credentials_email(instance.email, instance.registration_id, raw_password)
#     logger.info(f"Generated and set random password for user {instance.registration_id}")
            