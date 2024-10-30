from rest_framework import serializers
from django.db.models import Avg
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
     # atributo read_only seria apenas de leitura, não existindo no banco de dados esse field rate
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


    # Calcula a avaliação do filme
    def get_rate(self, obj):
        # aggregate() é uma função de agregação do Django ORM que realiza cálculos em um conjunto de registros, como soma, média, contagem, etc.
        # Avg('stars') é uma função de agregação específica, que calcula a média dos valores do campo stars em todos os objetos do QuerySet reviews
        # O resultado de .aggregate(Avg('stars')) é um dicionário contendo o valor médio dos stars
        
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1) # Aredondamento de numeros float

        return None


        ### Inutilizado, para fins de verificação ou comparação de codigo.
        ################################################################
        # reviews = obj.reviews.all()

        # # Se existem reviews, calcula a média de estrelas
        # if reviews:
        #     sum_reviews = 0

        #     # Soma as estrelas de todos os reviews
        #     for review in reviews:
        #         sum_reviews += review.stars
        #     # Contagem de todas as estrelas de reviews
        #     reviews_count = reviews.count()
        #     # Calcula a média de estrelas
        #     return round(sum_reviews / reviews_count, 1) # Aredondamento de numeros float

        # return None


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