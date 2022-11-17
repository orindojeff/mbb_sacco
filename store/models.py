from django.db import models
from pkg_resources import _

from accounts.models import User


#
# class Customer(User):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=120, unique=True)
#     address = models.CharField(max_length=220)
#     created_date = models.DateField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name

#
# class Drop(models.Model):
#     name = models.CharField(max_length=120, unique=True)
#     created_date = models.DateField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name


class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    sortno = models.PositiveIntegerField(null=True)
    price = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    image = models.ImageField(default='non')
    created_date = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(_('Updated'), auto_now=True, null=True)
    brand = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICE = (
        ('pg', 'Pending'),
        ('dc', 'Decline'),
        ('ap', 'Approved'),
        ('ofd', 'Out for Delivery'),
        ('Dl', 'Delivered'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='pg')
    created_date = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(_('Updated'), auto_now=True, null=True)

    @property
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        total = (sum([item.get_total for item in order_items]))
        return total

    @property
    def get_cart_items(self):
        order_items = self.orderitem_set.all()
        total = (sum([item.quantity for item in order_items]))
        return total

    def __str__(self):
        return self.product.name


class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    driver_name = models.CharField(max_length=120)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.driver_name



