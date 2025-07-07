from rest_framework import serializers
from ..models.transaction_model import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ['id', 'payment_date']  # You can add others as needed
