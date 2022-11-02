from django.urls import path

from store import views

app_name = "store"

urlpatterns = [
    path('SM-dashboard', views.SM_dashboard, name='SM-dashboard')
]