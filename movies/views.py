from django.db.models import Count, Avg
# Importando restframework
from rest_framework import generics, views, response, status
# Obriga a requisição ter autenticação de usuário da API
from rest_framework.permissions import IsAuthenticated

# Importando o modelo Movie do app movies
from .models import Movie
from reviews.models import Review
from movies.serializers import MovieSerializer, MovieStatsSerializer
# Permissão Global do Django-Admin
from core.permissions import GlobalDefaultPermissions


# View API | List | Create
class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# View API | List Detail | Update | Delete
class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# Estatísticas de Movies
class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Movie.objects.all()

    def get(self, request):
        # Calcula a quantidade de filmes
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        data = {
            'total_movies': total_movies,
            'movies_by_genre': movies_by_genre,
            'total_reviews': total_reviews,
            'average_stars': round(average_stars, 1) if average_stars else 0,
        }

        # O serializer seria redundante e opcional usar, apenas se o objetivo de resultado na resposta precisar de fato
        serializer = MovieStatsSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        return response.Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )