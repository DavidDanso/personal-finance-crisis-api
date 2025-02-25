# serializers.py
from rest_framework import serializers
from .models import Budget, BudgetCategory, BudgetTransaction

# Serializer for BudgetTransaction model.
class BudgetTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetTransaction
        fields = ['id', 'amount', 'date', 'description']


# Serializer for BudgetCategory model.
class BudgetCategorySerializer(serializers.ModelSerializer):
    transactions = BudgetTransactionSerializer(many=True, read_only=True)

    class Meta:
        model = BudgetCategory
        fields = ['id', 'name', 'planned', 'actual', 'transactions']


# Simplified category serializer for nesting in budgets
class CategoryNestedSerializer(serializers.ModelSerializer):
    transactions = BudgetTransactionSerializer(many=True, read_only=True)

    class Meta:
        model = BudgetCategory
        fields = ['id', 'name', 'planned', 'actual', 'transactions']


# Serializer for Budget model.
class BudgetSerializer(serializers.ModelSerializer):
    categories = BudgetCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Budget
        fields = [
            'id', 'user', 'name', 'start_date', 'end_date', 
            'total_income', 'total_expenses', 'categories'
        ]

    
