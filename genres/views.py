import json
from django.http import JsonResponse
from genres.models import Genre

# O mesmo que acontece no form do template html para proteger o envio de dados
from django.views.decorators.csrf import csrf_exempt


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
            }, 
            status_code=201,
        )