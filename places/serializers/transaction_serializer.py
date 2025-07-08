from rest_framework import serializers
from ..models.booking_model import Booking
from ..models.tour_package_model import TourPackage

class TourPackageSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourPackage
        fields = ['id', 'name', 'price']

class TransactionSerializer(serializers.ModelSerializer):
    tour_package = TourPackageSimpleSerializer()
    user = serializers.StringRelatedField()

    class Meta:
        model = Booking
        fields = ['id', 'user', 'tour_package', 'booked_at']
