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
        
        logger.info(f"Creating/updating user with registration_id: {registration_id}")
        
        try:
            user = self.model.objects.get(registration_id=registration_id)
            logger.info(f"Existing user found with registration_id: {registration_id}")
 
            for key, value in extra_fields.items():
                setattr(user, key, value)
        except self.model.DoesNotExist:
            logger.info(f"Creating new user with registration_id: {registration_id}")
            if 'email' in extra_fields:
                extra_fields['email'] = self.normalize_email(extra_fields['email'])
            extra_fields['secure_id'] = generate_user_secure_id()
            user = self.model(registration_id=registration_id, **extra_fields)
        
        if not password:
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
            logger.info(f"Generated random password for user: {registration_id}")
        else:
            logger.info(f"Using provided password for user: {registration_id}")
        
        # Set the password for the user
        user.set_password(password)
        logger.info(f"Password set for user: {registration_id}")
        
        user.is_active = True
        user.save()
        
        # Save the user with the new password
        user.save(using=self._db)
        logger.info(f"User saved with registration_id: {registration_id}")
        
        # Generate QR code only for non-superusers
        if not user.is_superuser:
            self.generate_and_save_qr_code(user)
        
        # TODO: Implement email sending functionality here
        # send_password_email(user.email, password)
        
        logger.info(f"Returning user object for registration_id: {registration_id}")
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
        
    