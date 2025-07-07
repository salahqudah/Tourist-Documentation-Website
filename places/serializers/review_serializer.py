from rest_framework import serializers
from ..models import Review

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # show username instead of user_id

    class Meta:
        model = Review
        fields = '__all__'