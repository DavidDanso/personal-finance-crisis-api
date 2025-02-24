# serializers.py
from rest_framework import serializers
from .models import Budget, BudgetCategory, BudgetTransaction

# Serializer for BudgetTransaction model.
class BudgetTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetTransaction
        fields = ['id', 'amount', 'date', 'description']


# Serializer for BudgetCategory model.
# Includes nested transactions using BudgetTransactionSerializer.
class BudgetCategorySerializer(serializers.ModelSerializer):
    # Nested serializer for related transactions.
    # 'many=True' indicates that a category can have multiple transactions.
    # 'read_only=True' prevents editing transactions via the category endpoint.
    transactions = BudgetTransactionSerializer(many=True, read_only=True)
    budget_id = serializers.CharField(source='budget.id', read_only=True)
    budget_name = serializers.CharField(source='budget.name', read_only=True)

    class Meta:
        model = BudgetCategory
        fields = ['id', 'budget_id', 'budget_name', 'name', 'planned', 'actual', 'transactions']


# Simplified category serializer for nesting in budgets
class CategoryNestedSerializer(serializers.ModelSerializer):
    transactions = BudgetTransactionSerializer(many=True, read_only=True)

    class Meta:
        model = BudgetCategory
        fields = ['id', 'name', 'planned', 'actual', 'transactions']

        
# Serializer for Budget model.
# Includes nested categories using BudgetCategorySerializer.
class BudgetSerializer(serializers.ModelSerializer):
    # Nested serializer for related categories.
    # 'many=True' indicates that a budget can have multiple categories.
    categories = BudgetCategorySerializer(many=True)

    class Meta:
        model = Budget
        fields = [
            'id', 'user', 'name', 'start_date', 'end_date', 
            'total_income', 'total_expenses', 'categories'
        ]

    
