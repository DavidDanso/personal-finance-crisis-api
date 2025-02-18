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

        # Sample categories with planned amounts
        categories_data = [
            ('Housing', Decimal('1500.00')),
            ('Groceries', Decimal('500.00')),
            ('Transportation', Decimal('300.00')),
            ('Utilities', Decimal('200.00')),
            ('Entertainment', Decimal('150.00')),
            ('Healthcare', Decimal('200.00')),
            ('Savings', Decimal('1000.00')),
            ('Shopping', Decimal('250.00'))
        ]

        # Create budgets for the next 3 months
        start_date = date.today().replace(day=1)
        for month in range(3):
            # Calculate budget period
            budget_start = start_date + timedelta(days=30*month)
            budget_end = (budget_start + timedelta(days=30)).replace(day=1) - timedelta(days=1)
            
            # Calculate totals
            total_planned = sum(amount for _, amount in categories_data)
            
            # Create budget
            budget = Budget.objects.create(
                user=user,
                name=f"Budget for {budget_start.strftime('%B %Y')}",
                start_date=budget_start,
                end_date=budget_end,
                total_income=total_planned + Decimal('500.00'),  # Buffer of 500
                total_expenses=total_planned,
                created_at=timezone.now(),
                updated_at=timezone.now()
            )

            # Create categories and transactions
            for category_name, planned_amount in categories_data:
                category = BudgetCategory.objects.create(
                    budget=budget,
                    name=category_name,
                    planned=planned_amount,
                    actual=Decimal('0.00')
                )

                # Create 2-4 transactions per category
                num_transactions = random.randint(2, 4)
                total_actual = Decimal('0.00')
                
                for _ in range(num_transactions):
                    transaction_amount = Decimal(str(random.uniform(
                        float(planned_amount) * 0.1,  # Min 10% of planned
                        float(planned_amount) * 0.5   # Max 50% of planned
                    ))).quantize(Decimal('.01'))
                    
                    transaction_date = budget_start + timedelta(
                        days=random.randint(0, (budget_end - budget_start).days)
                    )
                    
                    BudgetTransaction.objects.create(
                        category=category,
                        amount=transaction_amount,
                        date=transaction_date,
                        description=f"{category_name} Expense {_ + 1}"
                    )
                    
                    total_actual += transaction_amount
                
                # Update category actual amount
                category.actual = total_actual
                category.save()

        self.stdout.write(self.style.SUCCESS('Successfully created sample budget data'))