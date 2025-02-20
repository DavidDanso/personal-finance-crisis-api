from django.db import models
from accounts.models import User
import uuid


# Budget Management Models
class Budget(models.Model):
    # Links budget to a specific user (one user can have many budgets)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Name of the budget (e.g., "January 2024 Budget", "Holiday Budget")
    name = models.CharField(max_length=255)
    
    # Budget period
    start_date = models.DateField()  # When budget starts
    end_date = models.DateField()    # When budget ends
    
    # Financial totals
    total_income = models.DecimalField(max_digits=10, decimal_places=2)   # Total planned income
    total_expenses = models.DecimalField(max_digits=10, decimal_places=2)  # Total planned expenses
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)  # When budget was created
    updated_at = models.DateTimeField(auto_now=True)      # When budget was last modified
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"{self.name} ({self.start_date} to {self.end_date})"



# BudgetCategory model
class BudgetCategory(models.Model):
    # Links category to a specific budget (one budget can have many categories)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='categories')
    
    # Category name (e.g., "Housing", "Groceries", "Transportation")
    name = models.CharField(max_length=100)
    
    # Financial tracking
    planned = models.DecimalField(max_digits=10, decimal_places=2)  # Planned spending for category
    actual = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Actual spending

    def __str__(self):
        return f"{self.name} ({self.budget.name}) - ${self.planned:.2f}"


# BudgetTransaction model
class BudgetTransaction(models.Model):
    # Links transaction to a specific category (one category can have many transactions)
    category = models.ForeignKey(BudgetCategory, on_delete=models.CASCADE)
    
    # Transaction details
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Transaction amount
    date = models.DateField()  # When transaction occurred
    description = models.CharField(max_length=255)  # Transaction description

    def __str__(self):
        return f"{self.description} - ${self.amount:.2f} ({self.category.name})"