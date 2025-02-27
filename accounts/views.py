from rest_framework import generics
from .models import Budget, BudgetCategory, BudgetTransaction
from django.shortcuts import get_object_or_404
from .serializers import BudgetSerializer, BudgetCategorySerializer, BudgetTransactionSerializer

#
class BudgetCreateAPIView(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


