from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie

class Review(models.Model):
  movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
  stars = models.IntegerField(
    validators= [
      MinValueValidator(0, 'Avaliation must not be minor than 0 stars'),
      MaxValueValidator(5, 'Avaliation must not be major than 5 stars')
    ]
  )
  comment = models.TextField(null=True, blank=True)

  def __str__(self):
    return self.movie