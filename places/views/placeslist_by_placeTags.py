from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.db.models import Q
from ..models import TouristPlace, Tag
from ..serializers import TouristPlaceSerializer

class PlacesListByTagsView(APIView):
    permission_classes = [permissions.AllowAny]  # Or IsAuthenticated if you want auth

    def get(self, request):
        # Accept multiple tags as query params, e.g. ?tags=beach,museum
        tags_param = request.query_params.get('tags')
        if not tags_param:
            return Response({"error": "Please provide 'tags' query parameter"}, status=status.HTTP_400_BAD_REQUEST)

        tag_names = [tag.strip() for tag in tags_param.split(',') if tag.strip()]
        if not tag_names:
            return Response({"error": "No valid tags provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Filter tags by name
        tags = Tag.objects.filter(name__in=tag_names)
        if not tags.exists():
            return Response({"error": "No tags matched the given names"}, status=status.HTTP_404_NOT_FOUND)

        # Filter TouristPlaces that have ANY of the tags (OR logic)
        places = TouristPlace.objects.filter(tags__in=tags).distinct()

        serializer = TouristPlaceSerializer(places, many=True)
        return Response(serializer.data)
