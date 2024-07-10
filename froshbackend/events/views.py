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

import pyzbar.pyzbar as pyzbar
import cv2 
import numpy

# from .models import Events
# from users.test import qr_maker, generate_user_secure_id
# from ..users.views import *
# from ..users.models import User


import threading
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
backends = [cv2.CAP_DSHOW, cv2.CAP_MSMF, cv2.CAP_VFW]

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
from django.views.decorators import gzip
from django.utils import timezone
@csrf_exempt
@login_required
class GeneratePassView(APIView):
    def post(self, request):
        user = request.User
        last_scanned = request.data.get('booking_time', timezone.now())
        if not user.is_authenticated:
            return Response({"error": "User must be authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
        
        else:
            user.is_booked=True
            user.last_scanned=datetime.now().time()
            sentence = "Ticket booked successfully"
            return json.dumps({"sentence": sentence})
        
        import cv2
import threading
from django.http import StreamingHttpResponse
from django.views.decorators.gzip import gzip_page
from django.shortcuts import render
from pyzbar import pyzbar
import cv2
import base64
from django.http import JsonResponse
from django.shortcuts import render
from pyzbar import pyzbar
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# class VideoCamera:
#     def __init__(self):
#         self.video = cv2.VideoCapture(0)

#     def __del__(self):
#         self.video.release()

#     def get_frame(self):
#         success, image = self.video.read()
#         if not success:
#             return None, None

#         _, buffer = cv2.imencode('.jpg', image)
#         jpg_as_text = base64.b64encode(buffer).decode()

#         decoded = pyzbar.decode(image)
#         qr_data = None
#         for obj in decoded:
#             qr_data = obj.data.decode('utf-8')
# <<<<<<< HEAD
#             break   
# =======
#             break  
# >>>>>>> branch1

#         return jpg_as_text, qr_data

# camera = None

# def scanner(request):
#     global camera
#     if camera is None:
#         camera = VideoCamera()

#     if request.headers.get('x-requested-with') == 'XMLHttpRequest':
# <<<<<<< HEAD
       
# =======
        
# >>>>>>> branch1
#         frame, qr_data = camera.get_frame()
#         if frame is None:
#             return JsonResponse({'error': 'Failed to capture frame'})
#         return JsonResponse({
#             'frame': frame,
#             'qr_data': qr_data
#         })
#     else:
# <<<<<<< HEAD
 
# =======
    
# >>>>>>> branch1
#         return render(request, 'website/scanner.html')

def qr_scanner_view(request):
    return render(request, 'website/qr_scanner.html')

@csrf_exempt
def process_qr(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        qr_data = data.get('qr_data')
        
        # Process the QR data as needed
        # For example, you might want to save it to the database
        
        return JsonResponse({'status': 'success', 'qr_content': qr_data})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})