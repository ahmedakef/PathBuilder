from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .serializers import PathSerializer
from paths.models import Path
from rest_framework import permissions
from .permissions import IsOwner

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Path.objects.all()
    serializer_class = PathSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner) # adding IsOwner doesn't work as it show my paths only

    def perform_create(self, serializer):
        """Save the post data when creating a new path."""
        serializer.save(creator = self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Path.objects.all()
    serializer_class = PathSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwner)
    lookup_field = 'slug'