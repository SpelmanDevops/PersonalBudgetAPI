from rest_framework.routers import DefaultRouter
from .views import IncomeViewSet, ExpenseViewSet, BudgetCategoryViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'income', IncomeViewSet)
router.register(r'expense', ExpenseViewSet)
router.register(r'budget-categories', BudgetCategoryViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = router.urls