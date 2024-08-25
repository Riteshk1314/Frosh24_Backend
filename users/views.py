from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from hoods.models import Hoods
from django.contrib.auth import authenticate
from users.models import User
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
)
# import openpyxl

from events.serializers import UserSerializer 
# Create your views here.
class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            registration_id = request.data['registration_id']
            password = request.data['password']
        except KeyError:
            return Response({'error': 'registration_id and password are required'}, status=HTTP_400_BAD_REQUEST)
        user = authenticate(registration_id=registration_id, password=password)
        if not user:
            return Response({'error': 'Invalid credentials'}, status=HTTP_401_UNAUTHORIZED)
        token, _ = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user)
        print("success post")
        return Response({
            'token': token.key,
            'user': serializer.data,
        }, status=HTTP_200_OK)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
import random
import string


class ForgotPassword(APIView):
    def post(self, request):
        registration_id = request.data.get('registration_id')
        
        try:
            user = User.objects.get(registration_id=registration_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        email = user.email
        if not email:
            return Response({'error': 'User has no associated email'}, status=status.HTTP_400_BAD_REQUEST)
        
        new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        
        user.set_password(new_password)
        user.save()
        
        subject = 'Password Reset'
        message = f'Your new password is: {new_password}'
        from_email = 'riteshkapoor1314@gmail.com'
        recipient_list = [email]
        
        try:
            send_mail(subject, message, from_email, recipient_list)
        except Exception as e:
            return Response({'error': 'Failed to send email'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'message': 'New password sent to your email'}, status=status.HTTP_200_OK)
# import string
# import random
# import csv
# import logging

from django.db import transaction
# #  # Make sure to import your custom User model

# #  logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# def generate_random_password(length=10):
#     digits = string.digits
#     password = ''.join(random.choice(digits) for _ in range(length))
#     return password
# def generate_random_secure_id(length=8):
#     digits = string.digits
#     secure_id = ''.join(random.choice(digits) for _ in range(length))
#     return secure_id

# def csv_db():
#     input_csv_file = 'freshers.csv'
#     output_csv_file = 'user_data_with_secure_ids.csv'
#     # logging.info(f"Opening input CSV file: {input_csv_file}")
    
#     row_count = 0

#     try:
#         with open(input_csv_file, 'r', newline='', encoding='utf-8') as input_csvfile, \
#              open(output_csv_file, 'w', newline='', encoding='utf-8') as output_csvfile:
            
#             csvreader = csv.reader(input_csvfile)
#             csvwriter = csv.writer(output_csvfile)
            
#             # Write header to output CSV
#             csvwriter.writerow(['Name', 'Registration ID', 'Email', 'Image Path', 'Secure ID'])
            
#             start = int(input('Enter start row number: '))
#             for row_num, row in enumerate(csvreader, start=0):
#                 if row_num < start:
#                     continue
                
#                 if len(row) != 4:
#                     logging.warning(f"Skipping row {row_num}: Invalid number of columns")
#                     continue
                
#                 name, registration_id, email, image_path = row
#                 secure_id = generate_random_secure_id()
            
#                 print(f"Processing: {name}, {registration_id}, {secure_id}")
#                 logging.info(f"Generated values for row {row_num}: secure_id={secure_id}")
                
#                 try:
#                     with transaction.atomic():
#                         custom_user = User.objects.create(
#                             name=name,
#                             email=email,
#                             registration_id=registration_id,
#                             image=image_path,
#                             secure_id=secure_id,
#                             is_active=True,
#                             is_superuser=False,
#                             password=None,
#                             events=[]
#                         )
                        
#                         # csvwriter.writerow([name, registration_id, email, image_path, secure_id])
#                         #  # Set an unusable password
#                         custom_user.save()
                        
#                     row_count += 1
#                     logging.info(f"Successfully created user and added to CSV for row {row_num}")
#                 except Exception as e:
#                     logging.error(f"Error processing row {row_num}: {e}")

#         logging.info(f"Total rows added to output CSV: {row_count}")

#         # Verify the output CSV file
#         with open(output_csv_file, 'r', newline='', encoding='utf-8') as verify_file:
#             verify_reader = csv.reader(verify_file)
#             verify_row_count = sum(1 for row in verify_reader) - 1  # Subtract 1 for the header
#         logging.info(f"Verification: Output CSV file has {verify_row_count} rows (excluding header)")

#     except FileNotFoundError:
#         logging.error(f"CSV file '{input_csv_file}' not found.")
#     except Exception as e:
#         logging.error(f"An unexpected error occurred: {e}")

#     logging.info("Data processing completed")

# csv_db()