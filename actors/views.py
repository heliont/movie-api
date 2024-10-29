from rest_framework import generics
from actors.models import Actor
from actors.serializers import ActorSerializer


# View API | List | Create
class ActorCreateListView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class =  ActorSerializer


# View API | List Detail | Update | Delete
class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class =  ActorSerializer