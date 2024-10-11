import json
from django.http import JsonResponse
from genres.models import Genre

# Importando rest framwork
from rest_framework import generics
from genres.serializers import GenreSerializer

# O mesmo que acontece no form do template html para proteger o envio de dados
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404


class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer



@csrf_exempt
def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk)

    if request.method == 'GET':

        data = {'id': genre.id, 'name': genre.name}
        return JsonResponse(data)
    
    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data['name']
        genre.save()

        return JsonResponse(
            {
                'id': genre.id,
                'name': genre.name
            },
            status_code=200,
        )

    elif request.method == 'DELETE':
        genre.delete()
        return JsonResponse(
            { 'message': 'Gênero excluído com sucesso.'}
            #status_code=204,
        )