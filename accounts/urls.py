from django.urls import path, reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from accounts import views
from accounts.decorators import required_access
from accounts.views import (RiderCreateView,
                            CustomerLoginView,
                            LogoutView,
                            RiderLoginView,
                            UserCreateView,
                            password_change,
                            staff_login_view, customer_profile,
                            )

app_name = "accounts"

urlpatterns = [
    path('register/', UserCreateView.as_view(), name="register"),
    path('rider-register/', RiderCreateView.as_view(), name="rider-register"),
    path('login/', CustomerLoginView.as_view(), name="login"),
    path('rider-login/', RiderLoginView.as_view(), name="rider-login"),
    path('logout/', LogoutView.as_view(), name="logout"),

    # staff urls
    path('staff-login/', views.staff_login_view, name='staff-login'),
    path('sales-manager/', views.sales_manager, name='sales-manager'),
    path('finance-manager/', views.finance_manager, name='finance-manager'),
    path('driver/', views.driver, name='driver'),
    path('customer-profile', customer_profile, name='customer'),
    path('change-password', password_change, name='change-password'),
    path('customer-profile', customer_profile, name='customer-profile'),
    path('rider/', required_access(function=TemplateView.as_view(template_name="rider.html"),
                                   login_url=reverse_lazy('accounts:rider-login'), user_type="RD"), name="index"),
]
