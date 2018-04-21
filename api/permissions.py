from rest_framework.permissions import BasePermission
from paths.models import Path

class IsOwner(BasePermission):
    """Custom permission class to allow only path owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the path owner."""
        print(obj.creator == request.user)
        if isinstance(obj, Path):
            return obj.creator == request.user
        return obj.creator == request.user