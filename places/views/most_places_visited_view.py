# views/most_visited_places_view.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.db.models import Count, Q

from ..models import TouristPlace
from ..serializers import TouristPlaceSerializer  # Or a custom summary serializer if needed

class MostVisitedPlacesView(APIView):
    """
    GET /api/places/most-visited/
    Returns a list of tourist places ordered by number of confirmed bookings.
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        places = (
            TouristPlace.objects.annotate(
                num_visits=Count("tourpackage__bookingstatus", filter=Q(tourpackage__bookingstatus__status="confirmed"))
            )
            .order_by("-num_visits")
        )
        serializer = TouristPlaceSerializer(places, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
