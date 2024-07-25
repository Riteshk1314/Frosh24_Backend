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
    from google.cloud import storage

    qr_value = f"Registration ID: {user.registration_id}"
    qr_file_path = qr_maker(qr_value, user.registration_id)

    # Initialize Google Cloud Storage client
    storage_client = storage.Client()

    # Get the bucket
    bucket_name = 'your-bucket-name'  # Replace with your actual bucket name
    bucket = storage_client.bucket(bucket_name)

    # Define the destination blob name (file path in GCS)
    destination_blob_name = f'qr_codes/{user.registration_id}.png'

    # Create a blob object and upload the file
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(qr_file_path)

    # Generate a public URL (if your bucket is configured for public access)
    gcs_url = f'https://storage.googleapis.com/{bucket_name}/{destination_blob_name}'

    # Update user's qr field with the GCS URL
    user.qr = gcs_url
    user.save(update_fields=['qr'])

    # Delete the local file after upload
    os.remove(qr_file_path)
        
    