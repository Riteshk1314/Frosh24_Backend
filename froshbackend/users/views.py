from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
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