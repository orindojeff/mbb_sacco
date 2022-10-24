from django.contrib import admin

from .models import (
    Buyer,
    Drop,
    Product,
    Order,
    Delivery
)


class BuyerAdmin(admin.ModelAdmin):
    list_display = [ 'user', 'name', 'address', 'created_date' ]


admin.site.register(Buyer, BuyerAdmin)
admin.site.register(Drop)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Delivery)
