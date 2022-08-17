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
    password   = serializers.CharField()
    is_critic  = serializers.BooleanField(allow_null=True, default=False)
    updated_at = serializers.DateTimeField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True, default=False)

    def create(self, validated_data):

        user = User.objects.create(**validated_data)
        user.save()

        return user