from rest_framework import serializers
from .models import Budget, BudgetCategory, BudgetTransaction

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'user', 'name', 'start_date', 'end_date', 'total_income', 'total_expenses']



class BudgetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetCategory
        fields = ['id', 'budget', 'name', 'planned', 'actual']



class BudgetTransactionSerializer(serializers.ModelSerializer):
    # category = BudgetCategorySerializer()
    # category_name = serializers.CharField(source='category.name')
    class Meta:
        model = BudgetTransaction
        fields = ['id', 'category', 'amount', 'date', 'description']


