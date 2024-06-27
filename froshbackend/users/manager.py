from django.contrib.auth.base_user import BaseUserManager
import png, pyqrcode, os
import requests, base64, json
import random, string
from .test import generate_user_secure_id
class CustomUserManager(BaseUserManager):
    def create_user(self, registration_id, password=None, **extra_fields):
        counter = 0
        while True:
            try:
                if not registration_id:
                    raise ValueError("Registration ID is required!")
                
                extra_fields['email'] = self.normalize_email(extra_fields['email'])
                extra_fields['secure_id'] = generate_user_secure_id()
                user = self.model(registration_id=registration_id, **extra_fields)
                if not extra_fields['is_superuser']:
                    user.set_password(''.join(random.choices(string.ascii_uppercase +
                            string.digits, k=10)))
                else:
                    user.set_password(password)
                user.is_active = True
                user.save(using=self.db)
                return user
            except :
                if counter <3:
                    counter+=1
                    pass 
                else:
                    break

