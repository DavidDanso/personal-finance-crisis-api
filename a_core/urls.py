from django.contrib import admin
from django.urls import path
from budgets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/budgets/', views.budget_list, name='budget_list'),
    path('api/categories/', views.budget_category_list, name='category_list'),
    path('api/transactions/', views.budget_transaction_list, name='transaction_list'),
]
