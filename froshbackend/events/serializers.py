from .models import Event
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
class eventSerializer(serializers.ModelSerializer):
    class meta:
        model=Event
        fields="__all__"
        
