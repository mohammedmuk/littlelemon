from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MenuItems
        fields = ['title', 'price', 'inventory']


class BookingSerializer(serializers.ModelSerializer):
    model = models.Booking
    fields = "__all__"