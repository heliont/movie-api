from rest_framework import generics
# Obriga a requisição ter autenticação de usuário da API
from rest_framework.permissions import IsAuthenticated

from reviews.models import Review
from reviews.serializers import ReviewSerializer
# Permissão Global do Django-Admin
from core.permissions import GlobalDefaultPermissions

# View API | List | Create
class ReviewCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# View API | List Detail | Update | Delete
class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer