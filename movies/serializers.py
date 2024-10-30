from rest_framework import serializers
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
     # atributo read_only seria apenas de leitura, não existindo no banco de dados esse field rate
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


    # Calcula a avaliação do filme
    def get_rate(self, obj):
        reviews = obj.reviews.all()

        # Se existem reviews, calcula a média de estrelas
        if reviews:
            sum_reviews = 0

            # Soma as estrelas de todos os reviews
            for review in reviews:
                sum_reviews += review.stars
            # Contagem de todas as estrelas de reviews
            reviews_count = reviews.count()
            # Calcula a média de estrelas
            return round(sum_reviews / reviews_count, 1) # Aredondamento de numeros float

        return None


    # Verificação de data minima de filmes
    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError("A data de lançamento não pode ser anterior a 1990.")
        return value


    # Verificação de quantidade de caracteres permitidos
    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError("O resumo não pode ter mais de 2 caracteres.")
        return value