from rest_framework import generics
from .models import Debt, Payment
from django.shortcuts import get_object_or_404
from .serializers import DebtSerializer, PaymentSerializer

#
class DebtCreateAPIView(generics.ListCreateAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer


#
class DebtDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer
    lookup_url_kwarg = 'debt_id'


# /api/debts/{debt_id}/payments
class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        debt_id = self.kwargs.get('debt_id')
        debt = get_object_or_404(Debt, id=debt_id, user=self.request.user)
        serializer.save(debt=debt)