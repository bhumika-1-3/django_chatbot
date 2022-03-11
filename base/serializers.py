from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import CustomUser


class UserCreateSerializer (UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('id','email', 'username', 'password','phone')