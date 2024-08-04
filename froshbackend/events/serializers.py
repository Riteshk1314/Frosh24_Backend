from .models import Events
from users.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
class eventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Events
        fields="__all__"
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__" 
        
class PassesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Events
        fields="__all__"