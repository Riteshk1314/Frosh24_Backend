from django.shortcuts import render
from .serializers import eventSerializer
from .models import Event
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
        events=Event.objects.all()
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
        events=Event.objects.get(pk=pk)
        serializer=eventSerializer(car)
        serializer_data=serializer.data
        return Response(serializer_data)
    
    if request.method=='PUT':
        try:
            
            event=Event.objects.get(pk=pk)
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
        event=Event.objects.get(pk=pk)
        event.delete()
        return Response(status=202)
        