from asyncore import write
import email
from .models import User
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id         = serializers.IntegerField(read_only=True)
    username   = serializers.CharField()
    email      = serializers.CharField()
    birthdate  = serializers.DateField()
    first_name = serializers.CharField()
    last_name  = serializers.CharField()
    bio        = serializers.CharField(allow_null=True, allow_blank=True, default=None)
    password   = serializers.CharField(write_only=True)
    is_critic  = serializers.BooleanField(allow_null=True, default=False)
    updated_at = serializers.DateTimeField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True, default=False)

    def validate_username(self, value: int):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('username already exists')

        return value

    def validate_email(self, value: int):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('email already exists')

        return value

    def create(self, validated_data):

        user = User.objects.create(**validated_data)
        user.set_password(user.password)
        user.save()

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)