from django.http import JsonResponse
from genres.models import Genre

# Create your views here.

def genre_view(request):
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