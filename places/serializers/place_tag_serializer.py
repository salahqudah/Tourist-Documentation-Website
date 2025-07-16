from rest_framework import serializers
from ..models.place_tag_model import PlaceTag

class PlaceTagSerializer(serializers.ModelSerializer):
    place_name = serializers.CharField(source='place.name', read_only=True)
    tag_name = serializers.CharField(source='tag.name', read_only=True)

    class Meta:
        model = PlaceTag
        fields = ['id', 'place', 'tag', 'place_name', 'tag_name', 'added_at']
