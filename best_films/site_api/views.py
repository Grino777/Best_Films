# from rest_framework.response import Response
# from rest_framework.views import APIView
from site_api.serializers import MoviesSerializer, UserSerializer
from rest_framework import generics
from films_app.models import Movie
from django.contrib.auth.models import User

# Create your views here.


class AllMoviesApiView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer


class UsersApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
