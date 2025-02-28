# serializers.py
from rest_framework import serializers
from .models import UserProfile
import json

class FlexibleJSONField(serializers.JSONField):
    def to_internal_value(self, data):
        if isinstance(data, str):
            try:
                return json.loads(data)
            except json.JSONDecodeError:
                return [item.strip() for item in data.split(',') if item.strip()]
        return super().to_internal_value(data)


# Serializer for UserProfileSerializer.
class UserProfileSerializer(serializers.ModelSerializer):
    financial_goals = FlexibleJSONField(
        help_text="Enter financial goals as a JSON array or a comma-separated string."
    )
    class Meta:
        model = UserProfile
        fields = ['monthly_income', 'monthly_expenses', 'emergency_fund',
                  'total_debt', 'risk_tolerance', 'financial_goals', 'created_at']