import json
from django.http import JsonResponse
from genres.models import Genre

# O mesmo que acontece no form do template html para proteger o envio de dados
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

# Create your views here.
@csrf_exempt
def genre_create_list_view(request):

    if request.method == 'GET':
        genres = Genre.objects.all()

        # Serialize to work
        #data = [{'id': genre.id, 'name': genre.name} for genre in genres]

        # List of genres in get endpoint
        data = []
        for genre in genres:
            data.append({
                'id': genre.id,
                'name': genre.name
            })
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genre(name=data['name'])
        new_genre.save()

        return JsonResponse(
            {
                'id': new_genre.id,
                'name': new_genre.name
            } # ,status_code=201,
        )


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