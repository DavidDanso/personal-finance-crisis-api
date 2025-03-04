from django.contrib import admin
from django.urls import path
from budgets import views as budget_views
from accounts import views as user_views
from debts import views as debt_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # UserProfile endpoints
    path('api/profile/', user_views.UserProfileDetailAPIView.as_view(), name='user-profile-details'),
    
    # Budget endpoints
    path('api/budgets/', budget_views.BudgetCreateAPIView.as_view(), name='budget-list-create'),
    path('api/budgets/<uuid:budget_id>/', budget_views.BudgetDetailAPIView.as_view(), name='budget-detail'),
    
    # Category and transaction endpoints
    path('api/budgets/<uuid:budget_id>/categories/', budget_views.CreateCategoryAPIView.as_view(), name='category-create'),
    path('api/budgets/<uuid:budget_id>/categories/<int:category_id>/', budget_views.CategoryDetailsAPIView.as_view(), name='category-details'),
    path('api/budgets/<uuid:budget_id>/categories/<int:category_id>/transactions/', budget_views.CreateTransactionAPIView.as_view(), name='transaction-create'),
    path('api/budgets/<uuid:budget_id>/categories/<int:category_id>/transactions/<int:transaction_id>/', budget_views.TransactionDetailsAPIView.as_view(), name='transaction-details'),

    # Debt endpoints
    path('api/debts/', debt_views.DebtCreateAPIView.as_view(), name='debt-list-create'),
    path('api/debts/<uuid:debt_id>/', debt_views.DebtDetailsAPIView.as_view(), name='debt-details'),

]