from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import UserModel
from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ValidationError

class LessThanValidator:
    def __init__(self, base):
        self.base = base
    
    def __call__(self, value):
        if len(value) < self.base:
            raise ValidationError({'error': f"Имя пользователя должно быть больше или равно символам {self.base}"})


class GreaterThanValidator:
    def __init__(self, base):
        self.base = base
    
    def __call__(self, value):
        if len(value) > self.base:
            raise ValidationError({'error': f"Имя пользователя должно быть меньше или равно символам {self.base}"})



class UserSerializer(serializers.ModelSerializer):  
    class Meta:
        model = UserModel
        fields = ['username', 'number', "city", 'event_date']
    
    username = serializers.CharField(validators=[LessThanValidator(3), GreaterThanValidator(24)])

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)