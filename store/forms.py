from django import forms

from .models import Product, Delivery


class CustomerForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'data-val': 'true',
        'data-val-required': 'Please enter name',
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'address',
        'data-val': 'true',
        'data-val-required': 'Please enter address',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'data-val': 'true',
        'data-val-required': 'Please enter email',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'username',
        'data-val': 'true',
        'data-val-required': 'Please enter username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'password',
        'data-val': 'true',
        'data-val-required': 'Please enter password',
    }))
    retype_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'retype_password',
        'data-val': 'true',
        'data-val-required': 'Please enter retype_password',
    }))


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sortno', 'image', 'price', 'quantity']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'name'
            }),
            'sortno': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'sortno'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control', 'id': 'image'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'price'
            }),

            'quantity': forms.NumberInput(attrs={
                'class': 'form-control', 'id': 'quantity'
            }),
        }


#
# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = [
#              'product', 'design', 'color', 'customer',
#         ]
#
#         widgets = {
#             'supplier': forms.Select(attrs={
#                 'class': 'form-control', 'id': 'supplier'
#             }),
#             'product': forms.Select(attrs={
#                 'class': 'form-control', 'id': 'product'
#             }),
#             'design': forms.TextInput(attrs={
#                 'class': 'form-control', 'id': 'design'
#             }),
#             'color': forms.TextInput(attrs={
#                 'class': 'form-control', 'id': 'color'
#             }),
#             'buyer': forms.Select(attrs={
#                 'class': 'form-control', 'id': 'buyer'
#             }),
#             'season': forms.Select(attrs={
#                 'class': 'form-control', 'id': 'season'
#             }),
#             'drop': forms.Select(attrs={
#                 'class': 'form-control', 'id': 'drop'
#             }),
#         }


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'

        widgets = {
            'order': forms.Select(attrs={
                'class': 'form-control', 'id': 'order'
            }),
            'courier_name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'courier_name'
            }),
        }
