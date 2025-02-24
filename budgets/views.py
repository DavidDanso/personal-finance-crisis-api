from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Budget, BudgetCategory, BudgetTransaction
from django.shortcuts import get_object_or_404
from .serializers import BudgetSerializer, BudgetCategorySerializer, BudgetTransactionSerializer

# Create your views here.
@api_view(['GET'])
def budget_list(request):
    budgets = Budget.objects.all()
    serializer = BudgetSerializer(budgets, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def budget_detail(request, id):
    budget = get_object_or_404(Budget, id=id)
    serializer = BudgetSerializer(budget)
    return Response(serializer.data)


@api_view(['GET'])
def category_list(request):
    categories = BudgetCategory.objects.all()
    serializer = BudgetCategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def transaction_list(request):
    transactions = BudgetTransaction.objects.all()
    serializer = BudgetTransactionSerializer(transactions, many=True)
    return Response(serializer.data)
