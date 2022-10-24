from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from accounts.forms import CustomerSignUpForm, CustomerAuthenticationForm
from accounts.models import User
from django.urls import reverse_lazy


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = "accounts/customer-registration.html"
    form_class = CustomerSignUpForm
    model = User
    success_message = "You've registered successfully"
    success_url = reverse_lazy('index')


class CustomerLoginView(SuccessMessageMixin, LoginView):
    template_name = 'accounts/customer-login.html'
    authentication_form = CustomerAuthenticationForm
    success_url = reverse_lazy('index')
    success_message = "You've logged in successfully"


class LogoutView(View):

    def get(self, *args, **kwargs):
        logout(self.request)
        messages.info(self.request, "You've logged out successfully.")
        return redirect('index')
