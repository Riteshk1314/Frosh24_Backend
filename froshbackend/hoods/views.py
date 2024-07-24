from django.shortcuts import render
from django.shortcuts import  HttpResponse, redirect
from .models import Hood
import random
import string
import json
from django.contrib import messages
from ..users.models import User
from datetime import datetime
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Hood
from ..users.models import User
from .serializers import HoodSerializer, UserSerializer
from django.db import transaction
import random
# Create your views here.

# def random_allotments():
#     active_users = User.objects.filter(is_active=True).exclude(hood__isnull=False)
#     hoods = [hood for hood in Hood.objects.all()]
#     counters = {
#         hoods[0]:0,
#         hoods[1]:0,
#         hoods[2]:0,
#         hoods[3]:0
#     }
#     count = 0
#     print(active_users.count())
#     max_members = int(active_users.count()/4)
#     for user in active_users:
#         while True:
#             user_hood = random.choice(hoods)
#             if counters[user_hood] < max_members:
#                 counters[user_hood] += 1
#                 count +=1 
#                 user.hood = user_hood
#                 user.save()
#                 print(f"[{count}] [{user_hood.name}] {user}")
#                 break
#     for hood in hoods:
#         hood.member_count = counters[hood]
#         hood.save()
#     # print(active_users.count())
    
    
from .serializers import HoodSerializer, UserSerializer, LeaderboardEntrySerializer

@api_view(['GET'])
def boh_leaderboard(request):
    hoods = Hood.objects.all().order_by('-points')
    serializer = LeaderboardEntrySerializer(
        [{'name': hood.name, 'points': hood.points} for hood in hoods], 
        many=True
    )
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def hood_leaderboard(request, hood_id):
    try:
        hood = Hood.objects.get(id=hood_id)
    except Hood.DoesNotExist:
        return Response({"error": "Hood not found"}, status=status.HTTP_404_NOT_FOUND)
    
    users = User.objects.filter(hood=hood).order_by('-hood_points')
    serializer = LeaderboardEntrySerializer(
        [{'name': user.name, 'points': user.hood_points} for user in users], 
        many=True
    )
    return Response(serializer.data)