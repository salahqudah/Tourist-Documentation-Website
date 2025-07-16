# serializers/booking_serializer.py

from rest_framework import serializers
from places.models.booking_model import Booking  # ✅ this is your real model
from places.models.tour_package_model import TourPackage  # for PK field

class BookingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    tour_package = serializers.PrimaryKeyRelatedField(queryset=TourPackage.objects.all())
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Booking  # ✅ NOT BookingStatus
        fields = '__all__'
