from django.contrib import admin
from .models import Income, Expense, BudgetCategory, Transaction

admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(BudgetCategory)
admin.site.register(Transaction)
