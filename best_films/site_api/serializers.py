from rest_framework import serializers
from films_app.models import Movie
from django.contrib.auth.models import User


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('original_title', 'movie_title', 'id', 'category')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'id', 'email', 'is_staff')
