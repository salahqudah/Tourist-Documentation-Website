from rest_framework import serializers
from ..models import TourPackage

class TourPackageSerializer(serializers.ModelSerializer):
    guide = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = TourPackage
        fields = '__all__'
