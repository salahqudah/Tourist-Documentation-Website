# views/review_list_view.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404

from ..models import TouristPlace, Review
from ..serializers import ReviewSerializer

class PlaceReviewListView(APIView):
    """
    GET /api/places/<uuid:place_id>/reviews/
    List all reviews for a specific tourist place.
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, place_id):
        place = get_object_or_404(TouristPlace, id=place_id)
        reviews = Review.objects.filter(place=place).order_by("-created_at")
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
