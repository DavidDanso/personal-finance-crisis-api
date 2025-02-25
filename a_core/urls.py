from django.contrib import admin
from django.urls import path
from budgets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Budget endpoints
    path('api/budgets/', views.BudgetCreateAPIView.as_view(), name='budget-list-create'),
    path('api/budgets/<uuid:budget_id>/', views.BudgetDetailAPIView.as_view(), name='budget-detail'),
    
    # Category and transaction endpoints
    path('api/categories/', views.category_list, name='category_list'),
    path('api/transactions/', views.transaction_list, name='transaction_list'),
]