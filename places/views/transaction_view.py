from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from ..models.booking_model import Booking
from ..serializers.transaction_serializer import TransactionSerializer

class TransactionList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        transactions = Booking.objects.filter(user=request.user)

        if not transactions.exists():
            return Response({"detail": "No bookings found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
