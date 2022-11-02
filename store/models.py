from django.db import models
from accounts.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

#
# class Drop(models.Model):
#     name = models.CharField(max_length=120, unique=True)
#     created_date = models.DateField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name


class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    sortno = models.PositiveIntegerField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('out for delivery', 'Out for Delivery'),
        ('complete', 'Complete'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product.name


class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    driver_name = models.CharField(max_length=120)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.driver_name
