# serializers.py
from rest_framework import serializers
from .models import UserProfile

# Serializer for UserProfileSerializer.
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'monthly_income', 'monthly_expenses', 'emergency_fund',
                  'total_debt', 'risk_tolerance', 'financial_goals', 'created_at']