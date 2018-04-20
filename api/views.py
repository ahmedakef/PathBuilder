from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .serializers import PathSerializer
from paths.models import Path

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Path.objects.all()
    serializer_class = PathSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new path."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Path.objects.all()
    serializer_class = PathSerializer
    lookup_field = 'slug'