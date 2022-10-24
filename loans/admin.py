from django.contrib import admin

from .models import (
    loanApplication,
    loanRepayment,
    savings)

admin.site.register(loanApplication)
admin.site.register(loanRepayment)
admin.site.register(savings)

