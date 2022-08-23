from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status
from rest_framework.exceptions import ValidationError
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from movies.models import Movie
from users.models import User
from .models import Review
from .serializers import ReviewSerializer
from .permissions import IsAdminOrCriticOrReadOnly

class ReviewView(APIView, PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrCriticOrReadOnly]

    def get(self, request: Request, movie_id: int):
        movie = get_object_or_404(Movie, id=movie_id)
        reviews = Review.objects.filter(movie_id=movie.id)
        result_page = self.paginate_queryset(reviews, request, view=self)
        serializer = ReviewSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request: Request, movie_id: int):
        movie = get_object_or_404(Movie, id=movie_id)
        critic = get_object_or_404(User, username=request.user)

        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(movie=movie, critic=critic)

        if Review.objects.filter(movie=movie, critic=critic).count() > 1:
            raise ValidationError({'detail': 'Review already exists.'})

        return Response(serializer.data, status.HTTP_201_CREATED)

class ReviewDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrCriticOrReadOnly]

    def get(self, request: Request, movie_id: int, review_id: int):
        movie = get_object_or_404(Movie, id=movie_id)
        review = get_object_or_404(Review, id=review_id)
        serializer = ReviewSerializer(review)

        return Response(serializer.data)

    def delete(self, request: Request, movie_id: int, review_id: int):
        review = get_object_or_404(Review, id=review_id)
        self.check_object_permissions(request, review)
        review.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)