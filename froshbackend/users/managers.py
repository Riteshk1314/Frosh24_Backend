import random
import string
from django.contrib.auth.models import BaseUserManager
from .utils import generate_user_secure_id
import logging

logger = logging.getLogger(__name__)

class CustomUserManager(BaseUserManager):
    def create_user(self, registration_id, password=None, **extra_fields):
        if not registration_id:
            raise ValueError("Registration ID is required!")
        
        logger.info(f"Creating user with registration_id: {registration_id}")
        
        if 'email' in extra_fields:
            extra_fields['email'] = self.normalize_email(extra_fields['email'])
        
        user = self.model(registration_id=registration_id, **extra_fields)
        
        if password:
            user.set_password(password)
        
        user.is_active = True
        user.save(using=self._db)
        
        logger.info(f"User created with registration_id: {registration_id}")
        return user

    def create_superuser(self, registration_id, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(registration_id, password, **extra_fields)
    
    
    
    def generate_and_save_qr_code(self, user):
        # Import here to avoid circular import
        from .utils import qr_maker
        from django.conf import settings
        import os

        qr_value = f"Registration ID: {user.registration_id}"
        qr_file_path = qr_maker(qr_value, user.registration_id)

        relative_path = os.path.join('qr_codes', os.path.basename(qr_file_path))
        full_path = os.path.join(settings.MEDIA_ROOT, relative_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        os.rename(qr_file_path, full_path)

        user.qr = os.path.join(settings.MEDIA_URL, relative_path)
        user.save(update_fields=['qr'])
        
    