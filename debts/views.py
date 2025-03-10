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


class PaymentCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        # Retrieve the debt_id from the URL and filter payments for that specific debt.
        debt_id = self.kwargs.get('debt_id')
        return Payment.objects.filter(debt__id=debt_id, user=self.request.user)

    def perform_create(self, serializer):
        # Retrieve the debt instance using the debt_id from the URL, ensuring it belongs to the current user.
        debt_id = self.kwargs.get('debt_id')
        debt = get_object_or_404(Debt, id=debt_id, user=self.request.user)
        # Save the new Payment with the associated debt and the current user.
        serializer.save(debt=debt, user=self.request.user)
