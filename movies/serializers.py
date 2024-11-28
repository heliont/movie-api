from rest_framework import serializers
from django.db.models import Avg
from movies.models import Movie

from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    # Verificação de data minima de filmes
    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError("A data de lançamento não pode ser anterior a 1990.")
        return value

    # Verificação de quantidade de caracteres permitidos
    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError("O resumo não pode ter mais de 200 caracteres.")
        return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    # Pega os dados de ID e name de actors e genres
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()

    # atributo read_only seria apenas de leitura, não existindo no banco de dados esse field rate
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    # Calcula a avaliação do filme
    def get_rate(self, obj):
        # aggregate() é uma função de agregação do Django ORM que realiza cálculos em um conjunto de registros, como soma, média, contagem, etc.
        # Avg('stars') é uma função de agregação específica, que calcula a média dos valores do campo stars em todos os objetos do QuerySet reviews
        # O resultado de .aggregate(Avg('stars')) é um dicionário contendo o valor médio dos stars

        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            # Aredondamento de numeros float
            return round(rate, 1)

        return None


# Serializer comum sem ter um model especificado
class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()
