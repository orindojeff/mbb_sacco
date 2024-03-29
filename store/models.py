from django.db import models
from pkg_resources import _

from accounts.models import User, Customer


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
    description = models.CharField(max_length=100, null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.discount = None

    def __str__(self):
        return self.name


class Order(models.Model):
    transaction_id = models.CharField(max_length=250, default=False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE,)
    completed = models.BooleanField(_('Completed'), default=False)
    is_active = models.BooleanField(_('Active'), default=False)  # true means complete
    is_archived = models.BooleanField(_('Archived'), default=False,
                                      help_text=_('Means the oder has been cancelled.'))  # order cancelled
    created_date = models.DateTimeField(_('Created'), auto_now_add=True, null=True)
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


class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    driver_name = models.CharField(max_length=120)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.driver_name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created = models.DateTimeField(_('Created'), auto_now_add=True, null=True)
    updated = models.DateTimeField(_('Updated'), auto_now=True, null=True)

    @property
    def get_price(self):
        price = self.product.price * self.product.discount
        return price

    @property
    def get_total(self):
        total = self.get_price * self.quantity
        return total


#
class OrderPayment(models.Model):
    transaction_id = models.CharField(max_length=250)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    mpesa = models.CharField(max_length=10, help_text="Mpesa Code e.g MXFTR432R5")
    phone = models.IntegerField(blank=True, null=True)
    # manager = models.ForeignKey(Finance Man, on_delete=models.CASCADE, null=True)
    amount = models.FloatField(default=0.0)
    confirmed = models.BooleanField(default=False, help_text="Means manager has confirmed payment")
    updated = models.DateTimeField(_('Updated'), auto_now=True, null=True)
    created = models.DateTimeField(_('Created'), auto_now_add=True, null=True)
