# import form as form
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from accounts.decorators import required_access
from accounts.forms import CustomerSignUpForm, CustomerAuthenticationForm, RiderSignUpForm, RiderAuthenticationForm, \
    StaffLoginForm, CustomerProfileForm, CustomerForm
from accounts.models import User, CustomerProfile
from django.urls import reverse_lazy

from store.models import Order


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
    success_url = reverse_lazy('rider')


class RiderLoginView(SuccessMessageMixin, LoginView):
    template_name = 'accounts/rider-login.html'
    authentication_form = RiderAuthenticationForm
    success_url = reverse_lazy('rider')
    success_message = "You've logged in successfully"


def staff_login_view(request):
    loginform = StaffLoginForm(request.POST or None)
    msg = ''

    if request.method == 'POST':
        if loginform.is_valid():
            username = loginform.cleaned_data.get('username')
            password = loginform.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.user_type == "FM":
                login(request, user)
                return redirect('accounts:finance-manager')
            elif user is not None and user.user_type == "SM":
                login(request, user)
                return redirect('accounts:sales-manager')
            elif user is not None and user.user_type == "DR":
                login(request, user)
                return redirect('accounts:driver')
            else:
                msg = 'invalid login credentials'
        else:
            msg = 'error validating form'
    return render(request, 'accounts/staff-login.html', {'form': loginform, 'msg': msg})


@required_access(login_url=reverse_lazy('accounts:staff-login'), user_type="SM")
def sales_manager(request):
    return render(request, 'sales-manager.html')


@required_access(login_url=reverse_lazy('accounts:staff-login'), user_type="FM")
def finance_manager(request):
    return render(request, 'finance-manager.html')


@required_access(login_url=reverse_lazy('accounts:staff-login'), user_type="DR")
def driver(request):
    return render(request, 'driver.html')


#Change password
def password_change(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important
            messages.success(request, 'Your password was successfully updated!')
        else:
            messages.info(request, 'Please correct the errors below.')
    return render(request, 'accounts/change-password.html', {'form': form})


#profile settings
# def profile_main(request):
#     p_form = FinanceProfileForm(instance=request.user.finance.financeprofile)
#     form = FinanceForm(instance=request.user.finance)
#     if request.method == "POST":
#         p_form = FinanceProfileForm(request.POST, request.FILES, instance=request.user.finance.financeprofile)
#         form = FinanceForm(request.POST, instance=request.user.finance)
#         if form.is_valid() and p_form.is_valid():
#             form.save()
#             p_form.save()
#             messages.success(request, "Your Profile has been updated!")
#     context = {
#         'p_form': p_form,
#         'form': form,
#     }
#     return render(request, 'finance/forms/profile.html', context)


def customer_profile(request):
    profile, created = CustomerProfile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        p_form = CustomerProfileForm(request.POST, request.FILES, instance=profile)
        form = CustomerForm(request.POST, instance=request.user)
    else:
        p_form = CustomerProfileForm(instance=profile)
        form = CustomerForm(instance=request.user)
    # order = Order.objects.filter(customer=customer, is_active=True, completed=False).first()
    context = {
        'p_form': p_form,
        'form': form,
        # 'order': order
    }
    return render(request, 'accounts/profile.html', context)

