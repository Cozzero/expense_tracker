from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    transaction_types = [
        ('credit', 'Credit'),
        ('debt', 'Debt'),
    ]
    tax_types = [
        ('flat', 'Flat'),
        ('percentage', 'Percentage'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=transaction_types)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax_type = models.CharField(max_length=10, choices=tax_types, default='flat')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    @property
    def total(self):
        if self.tax_type == 'flat':
            return self.amount + self.tax
        elif self.tax_type == 'percentage':
            return self.amount + (self.amount * self.tax / 100)
        return self.amount
    
    def __str__(self):
        return f"{self.title} - {self.amount} - ({self.transaction_type})"