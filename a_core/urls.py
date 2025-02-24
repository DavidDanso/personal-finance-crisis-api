from django.contrib import admin
from django.urls import path
from budgets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Budget endpoints
    path('api/budgets/', views.budget_list, name='budget-list'),
    path('api/budgets/<uuid:id>/', views.budget_detail, name='budget-detail'),
    
    # Category and transaction endpoints
    path('api/categories/', views.category_list, name='category_list'),
    path('api/transactions/', views.transaction_list, name='transaction_list'),
]