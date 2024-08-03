from rest_framework import serializers
from .models import Hoods
from users.models import User

class HoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hoods
        fields = ['id', 'name', 'points']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'hood_points']