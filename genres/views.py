import json
from django.http import JsonResponse

# Importando restframework
from rest_framework import generics
# Obriga a requisição ter autenticação de usuário da API
from rest_framework.permissions import IsAuthenticated

# Importando o modelo Genre do app genres
from genres.models import Genre
from genres.serializers import GenreSerializer
from genres.permissions import GenrePermissionClass


class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GenrePermissionClass,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GenrePermissionClass,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def delete(self, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
            return JsonResponse({'message': 'Genre deletado com sucesso.'}, status=204)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500) 