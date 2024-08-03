from django.shortcuts import render
from django.shortcuts import  HttpResponse, redirect
from hoods.models import Hoods
import random
import string
import json
from django.contrib import messages
from users.models import User
from datetime import datetime
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from hoods.models import Hoods
from users.models import User
from hoods.serializers import HoodSerializer, UserSerializer
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
    
    
from hoods.serializers import HoodSerializer, UserSerializer

# @api_view(['GET'])
# def boh_leaderboard(request):
#     hoods = Hood.objects.all().order_by('-points')
#     serializer = LeaderboardEntrySerializer(
#         [{'name': hood.name, 'points': hood.points} for hood in hoods], 
#         many=True
#     )
#     return Response(serializer.data)

@api_view(['POST'])
def hood_leaderboard(request):
    if request.method != 'POST':
        return Response({"error": "Only POST requests are allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    registration_id = request.data.get('registration_id')
    if not registration_id:
        return Response({"error": "Registration ID is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(registration_id=registration_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    user_hood = user.hood 
    if not user_hood:
        return Response({"error": "User is not assigned to any hood"}, status=status.HTTP_404_NOT_FOUND)

    all_hoods = Hoods.objects.all().order_by('-points')
    serializer = HoodSerializer(all_hoods, many=True)

    response_data = {
        "user_hood": {
            "id": user_hood.id,
            "name": user_hood.name,
        },
        "profile_photo": user.image,
        "secure_id":user.secure_id,
        # "qr": user.qr,
        "all_hoodss": serializer.data
    }
    return Response(response_data)