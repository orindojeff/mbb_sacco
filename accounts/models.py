from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser):
    class UserTypes(models.TextChoices):
        DRIVER = 'DR', _('Driver')
        FINANCE_MANAGER = 'FM', _('Finance Manger')
        SALES_MANAGER = 'SM', _('Sales Manager')
        RIDER = 'RD', _('Rider')
        CUSTOMER = 'CM', _('Customer')

    user_type = models.CharField(
        max_length=2,
        choices=UserTypes.choices,
        default=UserTypes.CUSTOMER,
    )
    email = models.EmailField()
