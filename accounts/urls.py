from django.urls import path

from accounts.views import UserCreateView

app_name = "accounts"

urlpatterns = [
    path('register/', UserCreateView.as_view(), name="register"),
]
