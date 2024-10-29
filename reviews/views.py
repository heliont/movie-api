from rest_framework import generics
from reviews.models import Review
from reviews.serializers import ReviewSerializer


# View API | List | Create
class ReviewCreateListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# View API | List Detail | Update | Delete
class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer