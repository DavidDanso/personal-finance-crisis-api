# serializers.py
from rest_framework import serializers
from .models import Debt, Payment


# Serializer for DebtSerializer.
class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = ['user', 'id', 'lender', 'amount', 'interest_rate','due_date', 'status']



# Serializer for DebtSerializer.
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['user', 'id', 'amount', 'payment_date']