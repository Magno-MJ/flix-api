from rest_framework import serializers
from movies.models import Movie
from genres.models import Genre
from actors.models import Actor
from django.db.models import Avg

class MovieSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  title = serializers.CharField()
  genre = serializers.PrimaryKeyRelatedField(
    queryset = Genre.objects.all(),
  )
  release_date = serializers.DateField()
  actors = serializers.PrimaryKeyRelatedField(
    queryset = Actor.objects.all(),
    many = True,
  )
  resume = serializers.CharField()


class MovieListDetailSerializer(serializers.ModelSerializer):

  class Meta:
    model = Movie
    fields = '__all__'
    
class MovieModelSerializer(serializers.ModelSerializer):
  rate = serializers.SerializerMethodField(read_only=True)

  class Meta:
    model = Movie
    fields = '__all__'

  def get_rate(self, obj):
    rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

    if rate:
      return round(rate, 1)

    return None
  
  def validate_release_date(self, value):
    if value.year < 1990:
      raise serializers.ValidationError("The year must not be before 1990")
    return value

  def validate_resume(self, value):
    if len(value) > 200:
      raise serializers.ValidationError("The field resume must not be major than 200 chars")
    return value


class MovieStatsSerializer(serializers.Serializer):
  total_movies = serializers.IntegerField()
  movies_by_genre = serializers.ListField()
  total_reviews = serializers.IntegerField()
  average_stars = serializers.FloatField()

