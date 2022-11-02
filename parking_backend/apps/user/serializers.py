from django.contrib.auth.models import User
from rest_framework import serializers

from parking_backend.apps.user.models import MyUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class MyUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = MyUser
        fields = '__all__'
