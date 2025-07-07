from rest_framework import serializers
from ..models import TouristPlace

class TouristPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TouristPlace
        fields = '__all__'
