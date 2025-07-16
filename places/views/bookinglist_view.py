# views/booking_list_view.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from ..models import BookingStatus
from ..serializers import BookingSerializer

class BookingListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        bookings = BookingStatus.objects.filter(user=request.user)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
