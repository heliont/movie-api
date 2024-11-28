from rest_framework import generics
# Obriga a requisição ter autenticação de usuário da API
from rest_framework.permissions import IsAuthenticated

from actors.models import Actor
from actors.serializers import ActorSerializer
# Permissão Global do Django-Admin
from core.permissions import GlobalDefaultPermissions

# View API | List | Create
class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Actor.objects.all()
    serializer_class =  ActorSerializer


# View API | List Detail | Update | Delete
class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Actor.objects.all()
    serializer_class =  ActorSerializer