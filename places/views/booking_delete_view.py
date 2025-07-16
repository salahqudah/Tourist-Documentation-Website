# views/booking_delete_view.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from ..models import BookingStatus

class BookingDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        booking = get_object_or_404(BookingStatus, pk=pk, user=request.user)
        booking.delete()
        return Response({"detail": "Booking deleted."}, status=status.HTTP_204_NO_CONTENT)
