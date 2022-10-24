from django.db import models


class LoanApplication(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
    )
    amount = models.IntegerField(20)
    created_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    limit = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)


class Savings(models.Model):
    amount = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)


class LoanRepayment(models.Model):
    amount = models.IntegerField(20)
    created_date = models.DateField(auto_now_add=True)
    balance = models.IntegerField()
