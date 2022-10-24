from django.contrib import admin
from .models import User

admin.site.site_header = "MIGORI BODA BODA SACCO ADMIN "
admin.site.site_title = "Migori Boda Boda SACCO "
admin.site.index_title = "MIGORI BODA BODA SACCO"
admin.site.register(User)
