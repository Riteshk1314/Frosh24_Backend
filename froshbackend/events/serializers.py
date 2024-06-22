from .models import Events
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
class eventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Events
        fields="__all__"
        
