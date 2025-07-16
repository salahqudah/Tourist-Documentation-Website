# views/booking_add_view.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from drf_yasg.utils import swagger_auto_schema

from ..models import BookingStatus
from ..serializers import BookingSerializer

class BookingAddView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Add a new booking",
        request_body=BookingSerializer,
        responses={
            201: BookingSerializer,
            400: "Validation error"
        }
    )
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            booking = serializer.save(user=request.user)

            # Optional: If confirmed, increase visit_count
            if booking.status == 'confirmed':
                place = booking.tour_package.place
                place.visit_count += 1
                place.save(update_fields=["visit_count"])

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
