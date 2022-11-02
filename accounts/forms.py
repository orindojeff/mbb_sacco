from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, logout
from django.forms import forms
from django import forms

User = get_user_model()


class CustomerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = "CM"
        if commit:
            user.save()
        return user


class CustomerAuthenticationForm(AuthenticationForm):

    def clean(self):
        super().clean()
        if self.user_cache is not None and self.user_cache.is_staff or self.user_cache.user_type == "DR" or \
                self.user_cache.user_type == "FM" or self.user_cache.user_type == "SM" or \
                self.user_cache.user_type == "RD":
            logout(self.request)
            raise forms.ValidationError('Invalid username or password for customer login', code='invalid login')


class RiderSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = "CM"
        if commit:
            user.save()
        return user


class RiderAuthenticationForm(AuthenticationForm):

    def clean(self):
        super().clean()
        if self.user_cache is not None and self.user_cache.is_staff or self.user_cache.user_type == "DR" or \
                self.user_cache.user_type == "FM" or self.user_cache.user_type == "SM" or \
                self.user_cache.user_type == "CM":
            logout(self.request)
            raise forms.ValidationError('Invalid username or password for customer login', code='invalid login')


class FinanceManagerAuthenticationForm(AuthenticationForm):

    def clean(self):
        super().clean()
        if self.user_cache is not None and self.user_cache.is_staff or self.user_cache.user_type == "DR" or \
                self.user_cache.user_type == "RD" or self.user_cache.user_type == "SM" or \
                self.user_cache.user_type == "CM":
            logout(self.request)
            raise forms.ValidationError('Invalid username or password for customer login', code='invalid login')


class SalesManagerAuthenticationForm(AuthenticationForm):

    def clean(self):
        super().clean()
        if self.user_cache is not None and self.user_cache.is_staff or self.user_cache.user_type == "DR" or \
                self.user_cache.user_type == "FM" or self.user_cache.user_type == "RD" or \
                self.user_cache.user_type == "CM":
            logout(self.request)
            raise forms.ValidationError('Invalid username or password for customer login', code='invalid login')


class DriverAuthenticationForm(AuthenticationForm):

    def clean(self):
        super().clean()
        if self.user_cache is not None and self.user_cache.is_staff or self.user_cache.user_type == "RD" or \
                self.user_cache.user_type == "FM" or self.user_cache.user_type == "SM" or \
                self.user_cache.user_type == "CM":
            logout(self.request)
            raise forms.ValidationError('Invalid username or password for customer login', code='invalid login')


class StaffLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    #
    # class Meta:
    #     model = User
    #     fields = ('username', 'email', 'password1', 'password2', 'choices=UserTypes.choices,')