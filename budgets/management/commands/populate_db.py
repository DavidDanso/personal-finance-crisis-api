import random
from decimal import Decimal
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from accounts.models import User
from budgets.models import Budget, BudgetCategory, BudgetTransaction

class Command(BaseCommand):
    help = 'Creates sample budget data'

    def handle(self, *args, **kwargs):
        # Get or create user
        user = User.objects.filter(username='admin').first()
        if not user:
            user = User.objects.create_superuser(username='admin', password='test')

        # Basic categories with planned amounts
        categories_data = [
            ('Housing', Decimal('1500.00')),
            ('Groceries', Decimal('500.00'))
        ]

        # Create budgets for the next 6 months
        start_date = date(2025, 1, 1)  # Starting from January 2025
        for month in range(6):
            # Calculate budget period
            budget_start = start_date + timedelta(days=30*month)
            next_month = budget_start.month + 1 if budget_start.month < 12 else 1
            next_year = budget_start.year + 1 if next_month == 1 else budget_start.year
            budget_end = date(next_year, next_month, 1) - timedelta(days=1)
            
            # Calculate totals
            total_expenses = sum(amount for _, amount in categories_data)
            total_income = Decimal('4600.00')

            # Create budget
            budget = Budget.objects.create(
                user=user,
                name=f"Budget for {budget_start.strftime('%B %Y')}",
                start_date=budget_start,
                end_date=budget_end,
                total_income=total_income,
                total_expenses=Decimal('4100.00'),
                created_at=timezone.now(),
                updated_at=timezone.now()
            )

            # Create categories
            for name, planned in categories_data:
                actual = planned - Decimal(str(random.uniform(50, 100)))
                
                BudgetCategory.objects.create(
                    budget=budget,
                    name=name,
                    planned=planned,
                    actual=actual.quantize(Decimal('.01'))
                )

        self.stdout.write(self.style.SUCCESS('Successfully created sample budget data'))