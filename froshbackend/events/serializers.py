from .models import User,Events
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
class eventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Events
        fields="__all__"
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_booked', 'events']  