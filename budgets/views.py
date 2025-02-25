from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Budget, BudgetCategory, BudgetTransaction
from django.shortcuts import get_object_or_404
from .serializers import BudgetSerializer, BudgetCategorySerializer, BudgetTransactionSerializer

#
class BudgetCreateAPIView(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

#
class BudgetDetailAPIView(generics.RetrieveAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    lookup_url_kwarg = 'budget_id'



class CreateCategoryAPIView(generics.CreateAPIView):
    serializer_class = BudgetCategorySerializer

    def perform_create(self, serializer):
        budget = get_object_or_404(Budget, id=self.kwargs.get('budget_id'))
        serializer.save(budget=budget)



# POST /api/budgets/{budget_id}/categories/{category_id}/transactions/
class CreateTransactionAPIView(generics.CreateAPIView):
    serializer_class = BudgetTransactionSerializer

    def perform_create(self, serializer):
        budget_id = self.kwargs.get('budget_id')
        category_id = self.kwargs.get('category_id')

        # First verify the budget exists and belongs to the user
        budget = get_object_or_404(Budget, id=budget_id)
        
        # Then verify the category exists and belongs to the budget
        category = get_object_or_404(BudgetCategory, id=category_id, budget=budget)
        
        # Finally save the transaction with the category
        serializer.save(category=category)
