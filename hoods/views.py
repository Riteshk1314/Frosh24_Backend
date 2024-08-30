from django.shortcuts import render
from django.shortcuts import  HttpResponse, redirect
from hoods.models import Hoods
import random
import string
import json
# from events.models import passes
from events.models import Events
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
from events.models import passes
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
from django.http import JsonResponse

@api_view(['POST'])
def hood_leaderboard(request):
    if request.method != 'POST':
        return Response({"error": "Only POST requests are allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    registration_id = request.data.get('registration_id')
    if not registration_id:
        return Response({"error": "Registration ID is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(registration_id=registration_id)
        user_hood = user.hood_name
        event=Events.objects.filter(is_live=True).first()
        pass_users = passes.objects.filter(registration_id=user).filter(event_id=event).first()
    

        
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
    response_data = {
        "name":str(user.name),
        "profile_photo": str(user.image),
        "secure_id": str(user.secure_id),
        "pass_users": str(pass_users.event_id) if pass_users else "",
        "slot_test": str(pass_users.slot_test) if pass_users else "",
        "is_booked": str(pass_users.is_booked) if pass_users else "",
        "hood":str(user.hood_name) if user.hood_name else "",
    }
    # if not user_hood:
    #     return Response({"error": "User is not assigned to any hood"}, status=status.HTTP_404_NOT_FOUND)

    # all_hoods = Hoods.objects.all().order_by('-points')
    # serializer = HoodSerializer(all_hoods, many=True)
    
    # try:
    #     user_hood_obj = Hoods.objects.get(hood_name=user_hood)
    #     user_hood_serializer = HoodSerializer(user_hood_obj)
    # except Hoods.DoesNotExist:
    #     return Response({"error": "User's hood not found"}, status=status.HTTP_404_NOT_FOUND)
    # Hood=Hoods.objects.get(hood_name=user_hood)
    
    return Response(response_data)

# "user_hood": {
#             "id": user_hood_id,
#             "name": user_hood,
#         },
#         "profile_photo": str(user.image),
#         "secure_id": str(user.secure_id),  # Convert to string in case it's not
#         "all_hoods": serializer.data,
# import random
# from django.db import transaction
# from users.models import User
# from hoods.models import Hoods

# @transaction.atomic
# def distribute_users_to_hoods():
#     # Fetch the four hoods from the database
#     hood_names = [
#         "Duskborne keepers",
#         "Lunar serpants",
#         "Starlight sentinels",
#         "Celestial wardens"
#     ]
    
#     hoods = list(Hoods.objects.filter(hood_name__in=hood_names))

#     if len(hoods) != len(hood_names):
#         missing_hoods = set(hood_names) - set(hood.hood_name for hood in hoods)
#         print(f"Not all required hoods are present in the database. Missing hoods: {missing_hoods}")
#         return

#     # Fetch all users from the database
#     users = list(User.objects.all())

#     if not users:
#         print("No users found in the database.")
#         return

#     # Shuffle the users list to ensure random distribution
#     random.shuffle(users)

#     # Calculate the number of users per hood
#     users_per_hood = len(users) // len(hoods)

#     # Distribute users to hoods
#     distributed_hoods = {hood: [] for hood in hoods}

#     for i, user in enumerate(users):
#         hood_index = i % len(hoods)
#         hood = hoods[hood_index]
#         distributed_hoods[hood].append(user)
        
#         # Update user's hood_name field with the appropriate Hoods object
#         user.hood_name = hood
#         print(f"Assigning {user.name} to {hood.hood_name}")
#         user.save()

#     # Print the results
#     for hood, members in distributed_hoods.items():
#         print(f"{hood.hood_name}: {len(members)} members")
#         for user in members:
#             print(f"{user.name}")  # Assuming the User model has a 'username' field
#         print()

# # Call the function to distribute users
# distribute_users_to_hoods()


# @transaction.atomic
# def check_user_hoods():
#     # Get all users
#     all_users = User.objects.all()
    
#     # Get all valid hood names
#     valid_hood_names = set(Hoods.objects.values_list('hood_name', flat=True))
    
#     users_without_hood = []
#     users_with_invalid_hood = []
    
#     for user in all_users:
#         print("Checking user:", user.name)
#         if user.hood_name is None:
#             users_without_hood.append(user)
#         elif user.hood_name.hood_name not in valid_hood_names:
#             users_with_invalid_hood.append(user)
    
#     # Print results
#     print(f"Total users: {all_users.count()}")
#     print(f"Users without a hood: {len(users_without_hood)}")
#     print(f"Users with an invalid hood: {len(users_with_invalid_hood)}")
    
#     if users_without_hood:
#         print("\nUsers without a hood:")
#         for user in users_without_hood:
#             print(f"- {user.name} (ID: {user.id})")
    
#     if users_with_invalid_hood:
#         print("\nUsers with an invalid hood:")
#         for user in users_with_invalid_hood:
#             print(f"- {user.name} (ID: {user.id}, Invalid hood: {user.hood_name.hood_name})")
    
#     if not users_without_hood and not users_with_invalid_hood:
#         print("All users have valid hood assignments.")

# # Call the function to check user hoods
# # check_user_hoods()
# from django.db import transaction
# from django.db.models import Count
# from users.models import User
# from hoods.models import Hoods

# @transaction.atomic
# def count_users_per_hood():
#     # Get all hoods and annotate them with the count of users
#     hoods_with_counts = Hoods.objects.annotate(user_count=Count('users'))
    
#     # Get total number of users
#     total_users = User.objects.count()
    
#     # Print results
#     print("Users per hood:")
#     for hood in hoods_with_counts:
#         print(f"{hood.hood_name}: {hood.user_count} users")
    
#     # Count users without a hood
#     users_without_hood = User.objects.filter(hood_name__isnull=True).count()
    
#     print(f"\nUsers without a hood: {users_without_hood}")
#     print(f"Total users: {total_users}")
    
#     # Verify that the sum of users in hoods plus users without hood equals total users
#     sum_users_in_hoods = sum(hood.user_count for hood in hoods_with_counts)
#     if sum_users_in_hoods + users_without_hood == total_users:
#         print("\nAll users accounted for.")
#     else:
#         print("\nWarning: User count discrepancy detected.")
#         print(f"Sum of users in hoods ({sum_users_in_hoods}) + users without hood ({users_without_hood}) ≠ total users ({total_users})")

# # Call the function to count users per hood
# count_users_per_hood()