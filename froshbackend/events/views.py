from django.shortcuts import render
from .serializers import eventSerializer, UserSerializer
from events.models import Events, passes
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
import asyncio
from rest_framework.decorators import api_view, permission_classes
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
from rest_framework.permissions import IsAuthenticated
from datetime import date, time, datetime
from datetime import datetime
import random, string
import json
import sys
import os
import pyzbar.pyzbar as pyzbar
import cv2 
import numpy
from users.test import qr_maker, generate_user_secure_id
from users.views import *
from users.models import User
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import threading
from django.http import StreamingHttpResponse
from django.views.decorators.gzip import gzip_page
from django.shortcuts import render
from pyzbar import pyzbar
import cv2
import base64
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render
from pyzbar import pyzbar
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import threading
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
from django.db import transaction

# backends = [cv2.CAP_DSHOW, cv2.CAP_MSMF, cv2.CAP_VFW]

# @api_view(['GET','POST'])
# def EventList(request):
#     if request.method=='GET':
#         events=Events.objects.all()
#         serializer=eventSerializer(events,many=True)
#         return Response(serializer.data)
    
    
#     if request.method=='POST':
#         serializer=eventSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

class EventList(generics.ListCreateAPIView):
    queryset = Events.objects.all()
    serializer_class = eventSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

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





@api_view(['POST'])
@transaction.atomic
@permission_classes([IsAuthenticated])
def book_ticket(request):
    user = request.user
    name = request.data.get('name')
    
    if not name:
        return Response({"error": "Event name is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    event = get_object_or_404(Events, name=name, is_live=True)
    
    if passes.objects.filter(registration_id=user, event_id=event).exists():
        return Response({"error": "User already has a booked ticket"}, status=status.HTTP_400_BAD_REQUEST)
    
    if event.available_tickets <= 0:
        return Response({"error": "No tickets available for this event"}, status=status.HTTP_400_BAD_REQUEST)
    
    with transaction.atomic():
        new_pass = passes.objects.create(event_id=event, registration_id=user, is_booked=True)
        event.available_tickets -= 1
        event.save()
    
    serializer = UserSerializer(user)
    print("ticket booked successfully")
    return Response({
        "message": "Ticket booked successfully",
        "user": serializer.data,
        "event": {
            "name": event.name,
            "available_tickets": event.available_tickets
        }
    }, status=status.HTTP_200_OK)
    
    # user = request.user
    # name = request.data.get('name')
    
    # if not name:
    #     return Response({"error": "Event name is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    # event = get_object_or_404(Events, name=name, is_live=True)
    # secure_id = user.secure_id
    
    # if passes.objects.filter(secure_id=secure_id, event_id=event.event_id).exists():
    #     return Response({"error": "User already has a booked ticket"}, status=status.HTTP_400_BAD_REQUEST)
    
    # if event.available_tickets <= 0:
    #     return Response({"error": "No tickets available for this event"}, status=status.HTTP_400_BAD_REQUEST)
    
    # with transaction.atomic():
    #     new_pass = passes.objects.create(event=event, secure_id=secure_id, is_booked=True)
    #     event.available_tickets -= 1
    #     event.save()
    
    # serializer = UserSerializer(user)
    # print("ticket booked successfully")
    # return Response({
    #     "message": "Ticket booked successfully",
    #     "user": serializer.data,
    #     "event": {
    #         "name": event.name,
    #         "available_tickets": event.available_tickets
    #     }
    # }, status=status.HTTP_200_OK)
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
import traceback

@csrf_exempt
def qr_scanner_view(request):
    if request.method == 'GET':
        return render(request, 'website/qr_scanner.html')
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            qr_data = data.get('qr_data')
            
            print(f"Received QR data: {qr_data}")
            try:
                print("this try")
                secure_id = qr_data
                print(secure_id)
                user = User.objects.get(secure_id=secure_id)
                print(user)
                event = Events.objects.filter(is_live=True).first()
                print(event)
                
                event_pass = passes.objects.filter(
                event_id=event,registration_id=user).first()
                print(event_pass)
                if(event_pass.is_scanned==False):
                    event_pass.last_scanned = timezone.now()
                    event_pass.save()
                    event_pass.is_scanned=True
                    event_pass.save()
                    # print(f"scan success of {user.registration_id}")
                    return JsonResponse({
                        'success': True,
                        # 'registration_id': event_pass.registration_id,
                        'image':user.image,
                        'is_scanned': event_pass.is_scanned,
                        'is_booked': event_pass.is_booked,
                        'last_scanned': event_pass.last_scanned.isoformat(),
                        'message': 'User information retrieved successfully'
                    })
            except User.DoesNotExist:
                return JsonResponse({
                    'success': False,
                    'error': f'No user found with ID {qr_data}',
                    'message': 'Please check if the QR code contains a valid user ID'
                }, status=404)
            except ValueError:
                return JsonResponse({
                    'success': False,
                    'error': f'Invalid user ID format: {qr_data}',
                    'message': 'The QR code should contain a  secure ID'
                }, status=400)
            
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            # Log the full exception for debugging
            print(f"An unexpected error occurred: {str(e)}")
            print(traceback.format_exc())
            return JsonResponse({
                'success': False, 
                'error': 'An unexpected error occurred',
                'details': str(e)
            }, status=500)
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)