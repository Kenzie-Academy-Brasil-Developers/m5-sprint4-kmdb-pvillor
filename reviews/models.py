from django.db import models

class Recomendations(models.TextChoices):
    MUST_WATCH = "Must Watch"
    SHOULD_WATCH = "Should Watch"
    AVOID_WATCH = "Avoid Watch"
    DEFAULT = "No Opinion"

class Review(models.Model):
    stars = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField(default=False)
    recomendation = models.CharField(max_length=50, choices=Recomendations.choices, default=Recomendations.DEFAULT)
    critic = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="reviews")
    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE, related_name="reviews")