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


#
class CreateCategoryAPIView(generics.CreateAPIView):
    serializer_class = BudgetCategorySerializer

    def perform_create(self, serializer):
        budget = get_object_or_404(Budget, id=self.kwargs.get('budget_id'))
        serializer.save(budget=budget)


#
class CreateTransactionAPIView(generics.CreateAPIView):
    serializer_class = BudgetTransactionSerializer

    def perform_create(self, serializer):
        budget_id = self.kwargs.get('budget_id')
        category_id = self.kwargs.get('category_id')
        budget = get_object_or_404(Budget, id=budget_id)
        category = get_object_or_404(BudgetCategory, id=category_id, budget=budget)
        serializer.save(category=category)
