from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Budget
from .serializers import BudgetSerializer

# Create your views here.
@api_view(['GET'])
def budget_list(request):
    budgets = Budget.objects.all()
    serializer = BudgetSerializer(budgets, many=True)
    return Response(serializer.data)
