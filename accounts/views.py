# import form as form
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from accounts.forms import CustomerSignUpForm, CustomerAuthenticationForm, RiderSignUpForm, RiderAuthenticationForm, \
    StaffLoginForm
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


class RiderCreateView(SuccessMessageMixin, CreateView):
    template_name = "accounts/rider-registration.html"
    form_class = RiderSignUpForm
    model = User
    success_message = "You've registered successfully"
    success_url = reverse_lazy('rider-index')


class RiderLoginView(SuccessMessageMixin, LoginView):
    template_name = 'accounts/rider-login.html'
    authentication_form = RiderAuthenticationForm
    success_url = reverse_lazy('rider-index')
    success_message = "You've logged in successfully"


def staff_login_view(request):
    loginform = StaffLoginForm(request.POST or None)
    msg = None

    if request.method == 'POST':
        if loginform.is_valid():
            username = loginform.cleaned_data.get('username')
            password = loginform.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and request.user_type == "FM":
                login(request, user)
                return redirect('finance-manager')
            elif user is not None and request.user_cache.user_type == "SM":
                login(request, user)
                return redirect('sales-manger')
            elif user is not None and request.user_cache.user_type == "DR":
                login(request, user)
                return redirect('driver')
            else:
                msg = 'invalid login credentials'
        else:
            msg = 'error validating form'
    return render(request, 'accounts/staff-login.html', {'form': loginform, 'msg': msg})


def sales_manager(request):
    return render(request, 'sales-manager.html')


def finance_manager(request):
    return render(request, 'finance-manager.html')


def driver(request):
    return render(request, 'driver.html')
