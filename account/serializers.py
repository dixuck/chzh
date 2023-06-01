from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .models import CustomUser


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email')
