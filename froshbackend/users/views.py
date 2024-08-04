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
