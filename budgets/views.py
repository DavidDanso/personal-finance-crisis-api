from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Budget, BudgetCategory, BudgetTransaction
from django.shortcuts import get_object_or_404
from .serializers import BudgetSerializer, BudgetCategorySerializer, BudgetTransactionSerializer

# Create new budget.
class BudgetCreateAPIView(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class BudgetDetailAPIView(generics.RetrieveAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    lookup_url_kwarg = 'budget_id'



# Function-based views for category and transaction endpoints
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
