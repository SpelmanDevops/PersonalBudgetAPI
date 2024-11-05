from django.db import models
from django.contrib.auth.models import User

# Income Model
class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incomes')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.username} - Income: {self.amount} on {self.date}"

# Expense Model
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.username} - Expense: {self.amount} on {self.date}"

# Budget Category Model
class BudgetCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budget_categories')
    name = models.CharField(max_length=100)
    monthly_limit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__ (self):
        return f"{self.user.username} - Budget for {self.name}: {self.monthly_limit}"

# Transaaction Model
class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('INCOME', 'Income'),
        ('EXPENSE', 'Expense'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=100, blank=True)

    def __str__ (self):
        return f"{self.user.username} - {self.transaction_type}: {self.amount} on {self.date}"
