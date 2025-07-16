# views/review_create_view.py

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from drf_yasg.utils import swagger_auto_schema
from ..models import TouristPlace, BookingStatus, Review
from ..serializers import ReviewSerializer

class AddRatingView(APIView):
    """
    POST /api/reviews/
    Create one review per user per tourist place.
    The user must have a *confirmed booking* that includes this place.
    """
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Add a review to a tourist place",
        request_body=ReviewSerializer,
        responses={
            201: ReviewSerializer,
            400: "Validation error",
            403: "User has no confirmed booking for this place"
        }
    )
    def post(self, request):
        serializer = ReviewSerializer(data=request.data, context={"request": request})
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        place = serializer.validated_data["place"]
        rating_value = serializer.validated_data["rating"]

        # Ensure user has a confirmed booking for this place
        has_booking = BookingStatus.objects.filter(
            user=request.user,
            tour_package__place=place,
            status="confirmed"
        ).exists()

        if not has_booking:
            return Response(
                {"detail": "Only users with confirmed bookings can review this place."},
                status=status.HTTP_403_FORBIDDEN
            )

        # Prevent multiple reviews by the same user for the same place
        if Review.objects.filter(place=place, user=request.user).exists():
            return Response(
                {"detail": "You have already reviewed this place."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Save review and update place rating stats
        review = serializer.save(user=request.user)
        place.sum_of_ratings += rating_value
        place.number_of_ratings += 1
        place.total_rating = place.sum_of_ratings / place.number_of_ratings
        place.save(update_fields=["sum_of_ratings", "number_of_ratings", "total_rating"])

        return Response(ReviewSerializer(review).data, status=status.HTTP_201_CREATED)
