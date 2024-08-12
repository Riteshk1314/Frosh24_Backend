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
# import pyzbar.pyzbar as pyzbar
# import cv2 
# import numpy
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
# from pyzbar import pyzbar
# import cv2
# import base64
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render
# from pyzbar import pyzbar
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# import threading
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
    
    selected_fields = ['event_id', 'name', 'date', 'venue','is_booking','slot_id','is_live','image','is_display','time','description']  #
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
    
        # selected_data = []
        # print(serializer.data)
        # for item in serializer.data:
        #     if item['event_id'] in selected_data:
        #         selected_data[item['event_id']]['slots'].append({'date':item['date'], 'venue':item['venue'],'slot_id':item['slot_id'],'time':item['time']})
        #     else:
        #         selected_data[item['event_id']] = {
        #             'name':item['name'],
        #             'is_booking':item['is_booking'],
        #             'is_display':item['is_display'],
        #             'image': item['image'],
        #             'is_live': item['is_live'],
        #             'slots':[{'date':item['date'], 'venue':item['venue'],'slot_id':item['slot_id'],'time':item['time']}]
        #         }
        
        events_dict = {}
    
    # Process each serialized item
        for item in serializer.data:
            event_id = item['event_id']
            if event_id not in events_dict:
                # Initialize a new event entry
                events_dict[event_id] = {
                    'event_id': event_id,
                    'name': item['name'],
                    'is_booking': item['is_booking'],
                    'is_display': item['is_display'],
                    'image': item['image'],
                    'is_live': item['is_live'],
                    'slots': []
                }
            
            # Add slot information to the corresponding event
            events_dict[event_id]['slots'].append({
                'date': item['date'],
                'venue': item['venue'],
                'slot_id': item['slot_id'],
                'time': item['time']
            })
        
        # Convert the dictionary values to a list
        selected_data = list(events_dict.values())
        return Response(selected_data)
    
    
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



from django.db import transaction
from django.db.models import F
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def book_ticket(request):
    user = request.user
    name = request.data.get('name')
    slot_id=request.data.get('slot_id')
    
    if not name:
        return Response({"error": "Event name is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        with transaction.atomic():
            event = Events.objects.select_for_update().get(name=name, is_live=True,slot_id=slot_id)
            
            if passes.objects.filter(registration_id=user, event_id__event_id=event.event_id).exists():
                return Response({"error": "User already has a booked ticket"}, status=status.HTTP_400_BAD_REQUEST)
            
            if event.available_tickets <= 0 or not event.is_booking:
                return Response({"error": "No tickets available for this event"}, status=status.HTTP_400_BAD_REQUEST)
            
            new_pass = passes.objects.create(event_id=event, registration_id=user, is_booked=True,slot_test=slot_id)
     
            Events.objects.filter(id=event.id).update(available_tickets=F('available_tickets') - 1)
            
            event.refresh_from_db()
    
    except Events.DoesNotExist:
        return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = UserSerializer(user)
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

@csrf_exempt
@csrf_exempt
def qr_scanner_view(request):
    print("qr_scanner_view called")
    print(f"Request method: {request.method}")
    
    if request.method == 'GET':
        return render(request, 'website/qr_scanner.html')
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received POST data:", data)
            
            if 'qr_data' in data and 'action' in data:
                print("Calling handle_action")
                return handle_action(data)
            elif 'qr_data' in data:
                print("Calling handle_initial_scan")
                return handle_initial_scan(data)
            else:
                print("Invalid request data")
                return JsonResponse({
                    'success': False,
                    'error': 'Invalid request data',
                    'message': 'Request must contain qr_data and action for handle_action'
                }, status=400)
        
        except json.JSONDecodeError:
            print("JSONDecodeError")
            return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            # print(traceback.format_exc())
            return JsonResponse({
                'success': False, 
                'error': 'An unexpected error occurred',
                'details': str(e)
            }, status=500)
    else:
        print("Invalid request method")
        return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)
def handle_initial_scan(data):
    qr_data = data.get('qr_data')
    print(f"Received QR data: {qr_data}")
    try:
        secure_id = qr_data
        user = User.objects.get(secure_id=secure_id)
        print(f"User: {user.registration_id} (secure_id: {user.secure_id})")

        live_events = Events.objects.filter(is_live=True)
        if not live_events.exists():
            return JsonResponse({
                'success': False,
                'error': 'No live event found',
                'message': 'There is no active event at the moment'
            }, status=404)

        event = live_events.first()
        print(f"Selected event: {event.id} - {event.name}")

        print("Querying passes...")
        event_pass = passes.objects.get(registration_id=user, event_id=event)
        print(f"Event pass query result: {event_pass}")
        print(event_pass.event_id)

        print(event_pass.registration_id)
        if event_pass is None:
            return JsonResponse({
                'success': False,
                'error': 'No pass found for this user and event',
                'message': 'User does not have a pass for the current event'
            }, status=404)

        if not event_pass.is_scanned:
            event_pass.last_scanned = timezone.now()
            event_pass.save()

        return JsonResponse({
            'success': True,
            'event':event.name,
            'registration_id': user.registration_id,
            'image': user.image if hasattr(user, 'image') else None,
            'is_scanned': event_pass.is_scanned,
            'is_booked': event_pass.is_booked,
            'slot_test': event_pass.slot_test,
            'last_scanned': event_pass.last_scanned.isoformat(),
            'message': 'User information retrieved successfully'
        })

    except User.DoesNotExist:
        return JsonResponse({
            'success': False,
            'error': f'No user found with secure ID {qr_data}',
            'message': 'Please check if the QR code contains a valid secure ID'
        }, status=404)
    except ValueError:
        return JsonResponse({
            'success': False,
            'error': f'Invalid secure ID format: {qr_data}',
            'message': 'The QR code should contain a valid secure ID'
        }, status=400)
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return JsonResponse({
            'success': False,
            'error': 'An unexpected error occurred',
            'message': str(e)
        }, status=500)
        

def handle_action(data):
    qr_data = data.get('qr_data') 
    action = data.get('action')
    
    try:
        user = User.objects.get(secure_id=qr_data)
        event = Events.objects.filter(event_id__event_id=event.event_id)
        
        if not event:
            return JsonResponse({
                'success': False,
                'error': 'No live event found',
                'message': 'There is no active event at the moment'
            }, status=404)
        
        try:
            event_pass = passes.objects.get(registration_id=user, event_id__event_id=event.event_id)
        except passes.DoesNotExist:
            return JsonResponse({
                'success': False,
                'error': 'No pass found',
                'message': 'No pass found for this user and event'
            }, status=404)
        
        if action == 'accept':
            print("accept action tried")
            event_pass.is_scanned = True
            event_pass.last_scanned = timezone.now()
            print(event_pass.is_scanned)
            event_pass.save(update_fields=['is_scanned', 'last_scanned'])
            message = 'Scan accepted successfully'
        elif action == 'reject':
            event_pass.is_scanned = False
            event_pass.save(update_fields=['is_scanned'])
            message = 'Scan rejected successfully'
        else:
            return JsonResponse({
                'success': False,
                'error': 'Invalid action',
                'message': 'Action must be either "accept" or "reject"'
            }, status=400)
        
        print(f"After save: is_scanned = {event_pass.is_scanned}")
        
        return JsonResponse({
            'success': True,
            'message': message,
            'is_scanned': event_pass.is_scanned,
            'last_scanned': event_pass.last_scanned.isoformat() if event_pass.last_scanned else None
        })
    except User.DoesNotExist:
        return JsonResponse({
            'success': False,
            'error': f'No user found with secure ID {qr_data}',
            'message': 'User not found'
        }, status=404)
    except Exception as e:
        print(f"Unexpected error in handle_action: {str(e)}")
        # print(traceback.format_exc())
        return JsonResponse({
            'success': False,
            'error': 'An error occurred while processing the action',
            'details': str(e)
        }, status=500)