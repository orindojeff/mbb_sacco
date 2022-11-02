
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from accounts.decorators import customer_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', customer_required(TemplateView.as_view(template_name="index.html")), name="index"),
    path('', include('accounts.urls')),
    path('', include('store.urls')),
]
