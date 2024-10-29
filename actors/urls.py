from django.urls import path
from .views import *

urlpatterns = [
    # Views API para Atores
    path('actors/', ActorCreateListView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-view'),
]
