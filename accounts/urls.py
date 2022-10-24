from django.urls import path

from accounts.views import UserCreateView, CustomerLoginView, LogoutView

app_name = "accounts"

urlpatterns = [
    path('register/', UserCreateView.as_view(), name="register"),
    path('login/', CustomerLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
