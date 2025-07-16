from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from ..models.booking_model import Booking

parameter = openapi.Parameter(
    'obj', openapi.IN_QUERY,
    description="Must be 'booking'",
    type=openapi.TYPE_STRING,
    enum=['booking'],
    required=True
)

class ClearBookingView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(manual_parameters=[parameter])
    def delete(self, request, booking_id):
        obj = request.query_params.get('obj')

        if obj != 'booking':
            return Response({"error": "Invalid type. Only 'booking' is allowed."}, status=400)

        try:
            booking = Booking.objects.get(id=booking_id, user=request.user)
        except Booking.DoesNotExist:
            return Response({"error": "Booking not found."}, status=404)

        booking.delete()
        return Response({"message": f"Booking {booking_id} deleted successfully."}, status=200)
