# Importando restframework
from rest_framework import generics

# Importando o modelo Movie do app movies
from .models import Movie
from movies.serializers import MovieSerializer


# View API | List | Create
class MovieCreateListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# View API | List Detail | Update | Delete
class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer