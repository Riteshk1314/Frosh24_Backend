from rest_framework import serializers
from .models import Hood
from ..users.models import User

class HoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hood
        fields = ['id', 'name', 'points']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'hood_points']