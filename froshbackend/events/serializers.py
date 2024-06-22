from .models import Event
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
class eventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields="__all__"
        
