from django.contrib import admin

from .models import (
    # Customer,
    Product,
    Order,
    Delivery
)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sortno', 'price', 'quantity', 'image', 'created_date', 'brand')


# admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Delivery)
