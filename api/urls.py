from django.urls import path  # Import the path function
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token  # Import the obtain_auth_token view
from .views import IncomeViewSet, ExpenseViewSet, BudgetCategoryViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'income', IncomeViewSet)
router.register(r'expense', ExpenseViewSet)
router.register(r'budget-categories', BudgetCategoryViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    # Token authentication endpoint
    path('token/', obtain_auth_token, name='api_token'),
] + router.urls  # Include the routes from the DefaultRouter
