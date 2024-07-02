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
from decouple import config

from datetime import datetime

import random, string
import json



from ..users.test import qr_maker, generate_user_secure_id
from ..users.views import *
from ..users.models import User
from .models import Events

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
        