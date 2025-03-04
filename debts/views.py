from rest_framework import generics
from .models import Debt, Payment
from django.shortcuts import get_object_or_404
from .serializers import DebtSerializer

#
class DebtCreateAPIView(generics.ListCreateAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer


# /api/debts/{debt_id}
class DebtDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer
    lookup_url_kwarg = 'debt_id'
