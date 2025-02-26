from django.contrib import admin
from django.urls import path
from budgets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Budget endpoints
    path('api/budgets/', views.BudgetCreateAPIView.as_view(), name='budget-list-create'),
    path('api/budgets/<uuid:budget_id>/', views.BudgetDetailAPIView.as_view(), name='budget-detail'),
    
    # Category and transaction endpoints
    path('api/budgets/<uuid:budget_id>/categories/', views.CreateCategoryAPIView.as_view(), name='category-create'),
    path('api/budgets/<uuid:budget_id>/categories/<int:category_id>/', views.CategoryDetailsAPIView.as_view(), name='category-details'),
    path('api/budgets/<uuid:budget_id>/categories/<int:category_id>/transactions/', views.CreateTransactionAPIView.as_view(), name='transaction-create'),
    path('api/budgets/<uuid:budget_id>/categories/<int:category_id>/transactions/<int:transaction_id>/', views.TransactionDetailsAPIView.as_view(), name='transaction-detalis'),
]