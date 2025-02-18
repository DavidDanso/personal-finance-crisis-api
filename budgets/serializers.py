from rest_framework import serializers
from .models import Budget, BudgetCategory, BudgetTransaction

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'name', 'start_date', 'end_date', 'total_income', 'total_expenses', 'created_at']


