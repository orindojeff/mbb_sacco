from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from accounts.forms import CustomerSignUpForm
from accounts.models import User
from django.urls import reverse_lazy


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = "accounts/customer-registration.html"
    form_class = CustomerSignUpForm
    model = User
    success_message = "You've registered successfully"
    success_url = reverse_lazy('index')
