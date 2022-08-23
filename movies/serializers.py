from rest_framework import serializers
from genres.serializers import GenreSerializer
from .models import Movie
from genres.models import Genre

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    premiere = serializers.DateField()
    duration = serializers.CharField()
    classification = serializers.IntegerField()
    synopsis = serializers.CharField()
    genres = GenreSerializer(many=True)

    def create(self, validated_data):
        genres_list = validated_data.pop("genres")

        movie = Movie.objects.create(**validated_data)

        for genre_dict in genres_list:
            genre_obj, _ = Genre.objects.get_or_create(**genre_dict)
            movie.genres.add(genre_obj)

        movie.save()

        return movie

    def update(self, instance: Movie, validated_data: dict) -> Movie:
        genres_list = validated_data.pop("genres")

        for key, value in validated_data.items():
            if key == 'genres':
                for genre_dict in genres_list:
                    genre_obj, _ = Genre.objects.get(**genre_dict)
                    instance.genres.set(genre_obj)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance