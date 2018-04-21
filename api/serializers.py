from rest_framework import serializers
from paths.models import Path

class PathSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Path
        fields = ('id', 'name', 'slug', 'description','creator','updated','added','photo')
        read_only_fields = ('updated','added')
        lookup_field='slug'
