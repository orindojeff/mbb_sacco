from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import ProductForm, DeliveryForm
# # from users.models import User
# from accounts.models import User

from .models import (
    # Product,
    Order, Customer, Product, Delivery,

)
# from .forms import (
#     ProductForm,
#     OrderForm,
#     DeliveryForm
# )


# Create your views here.
# dashboard views
def SM_dashboard(request):
    return render(request, 'dashboard/salesmanager-dashboard.html')


#
# # Buyer views
# @login_required(login_url='login')
# def create_buyer(request):
#     forms = BuyerForm()
#     if request.method == 'POST':
#         forms = BuyerForm(request.POST)
#         if forms.is_valid():
#             name = forms.cleaned_data['name']
#             address = forms.cleaned_data['address']
#             email = forms.cleaned_data['email']
#             username = forms.cleaned_data['username']
#             password = forms.cleaned_data['password']
#             retype_password = forms.cleaned_data['retype_password']
#             if password == retype_password:
#                 user = User.objects.create_user(
#                     username=username, password=password,
#                     email=email, is_buyer=True
#                 )
#                 Buyer.objects.create(user=user, name=name, address=address)
#                 return redirect('buyer-list')
#     context = {
#         'form': forms
#     }
#     return render(request, 'store/create_buyer.html', context)
#
#
class CustomerListView(ListView):
    model = Customer
    template_name = 'store/customer-list.html'
    context_object_name = 'customer'


#
# # Product views
# @login_required(login_url='login')
def create_product(request):
    forms = ProductForm()
    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('product-list')
    context = {
        'form': forms
    }
    return render(request, 'store/add-product.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'store/product-list.html'
    context_object_name = 'product'


# Order views
# @login_required(login_url='login')
# def create_order(request):
#     forms = OrderForm()
#     if request.method == 'POST':
#         forms = OrderForm(request.POST)
#         if forms.is_valid():
#             supplier = forms.cleaned_data['supplier']
#             product = forms.cleaned_data['product']
#             design = forms.cleaned_data['design']
#             color = forms.cleaned_data['color']
#             buyer = forms.cleaned_data['buyer']
#             season = forms.cleaned_data['season']
#             drop = forms.cleaned_data['drop']
#             Order.objects.create(
#                 customer=customer,
#                 product=product,
#                 design=design,
#                 color=color,
#                 status='pending'
#             )
#             return redirect('order-list')
#     context = {
#         'form': forms
#     }
#     return render(request, 'store/create_order.html', context)


class OrderListView(ListView):
    model = Order
    template_name = 'store/order-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = Order.objects.all().order_by('-id')
        return context


# # Delivery views
# @login_required(login_url='login')
def create_delivery(request):
    forms = DeliveryForm()
    if request.method == 'POST':
        forms = DeliveryForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('delivery-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create-delivery.html', context)


class DeliveryListView(ListView):
    model = Delivery
    template_name = 'store/delivery-list.html'
    context_object_name = 'delivery'
