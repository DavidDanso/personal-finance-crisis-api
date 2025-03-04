# serializers.py
from rest_framework import serializers
from .models import Debt


# Serializer for DebtSerializer.
class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = ['user', 'id', 'lender', 'amount', 'interest_rate','due_date', 'status']