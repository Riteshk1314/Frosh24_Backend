from rest_framework import serializers
from .models import Hoods
from users.models import User

class HoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hoods
        fields = ['hood_id', 'hood_name', 'description', 'image', 'member_count', 'points']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"