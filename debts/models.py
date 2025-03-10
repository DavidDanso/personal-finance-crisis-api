from django.db import models
from accounts.models import User
from django.contrib.auth.models import User
import uuid

class Debt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lender = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    due_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[('active', 'Active'), ('paid', 'Paid'), ('overdue', 'Overdue')],
        default='active'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"{self.user.username} owes ${self.amount} to {self.lender}"

    class Meta:
        ordering = ['-created_at']


class Payment(models.Model):
    debt = models.ForeignKey(Debt, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} paid ${self.amount} on {self.payment_date}"

