from rest_framework import serializers
from users.models import User
from movies.serializers import MovieSerializer
from .models import  Review

class CriticSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']

class ReviewSerializer(serializers.ModelSerializer):
    critic = CriticSerializer(read_only=True)
    movie_id = MovieSerializer(read_only=True)['id']
    stars = serializers.IntegerField(min_value=1, max_value=10)

    class Meta:
        model = Review
        fields = ['id', 'stars', 'review', 'spoilers', 'recomendation', 'critic', 'movie_id']