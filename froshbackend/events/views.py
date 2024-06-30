from django.shortcuts import render
from .serializers import eventSerializer
from .models import Events
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins 
from rest_framework import generics 
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser,AllowAny,IsAuthenticated

@api_view(['GET','POST'])
def EventList(request):
    if request.method=='GET':
        events=Events.objects.all()
        serializer=eventSerializer(events,many=True)
        return Response(serializer.data)
    
    
    if request.method=='POST':
        serializer=eventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        

@api_view(['GET','PUT','DELETE'])
def EventView(request,pk):
    
    if request.method=='GET':
        event=Events.objects.get(pk=pk)
        serializer=eventSerializer(event)
        serializer_data=serializer.data
        return Response(serializer_data)
    
    if request.method=='PUT':
        try:
            
            event=Events.objects.get(pk=pk)
        except:
            return Response({'error':'event not found'},status=status.HTTP_404_NOT_FOUND)
        serializer=eventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer_data=serializer.data
            return Response(serializer_data)
        
        else:
            return Response(serializer.errors)
        
    if request.method=='DELETE':
        event=Events.objects.get(pk=pk)
        event.delete()
        return Response(status=202)
        
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

from datetime import date, time, datetime

from datetime import datetime

import random, string
import json
import sys
import os

# from .models import Events
# from users.test import qr_maker, generate_user_secure_id
# from ..users.views import *
# from ..users.models import User


from django.utils import timezone
@csrf_exempt
@login_required
class GeneratePassView(APIView):
    def post(self, request):
        user = request.User
        last_scanned = request.data.get('booking_time', timezone.now())
        if not user.is_authenticated:
            return Response({"error": "User must be authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
        
        # Generate a new pass for the user
        else:
            user.is_booked=True
            user.last_scanned=datetime.now().time()
            sentence = "Ticket booked successfully"
            return json.dumps({"sentence": sentence})
        
class scanner(APIView):
    def get(self, request):
        user = request.User
        
