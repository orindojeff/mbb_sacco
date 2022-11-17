from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView

from accounts.decorators import required_access
from utils.utils import generate_key
from .forms import ProductForm, DeliveryForm
# # from users.models import User


from .models import (
    # Product,
    Order, Product, Delivery
)


# from .forms import (
#     ProductForm,
#     OrderForm,
#     DeliveryForm
# )


# Create your views here.
# dashboard views
@required_access(login_url=reverse_lazy('accounts:staff-login'), user_type="SM")
def SM_dashboard(request):
    return render(request, 'dashboard/salesmanager-dashboard.html')


# class CustomerListView(ListView):
#     model = Customer
#     template_name = 'store/customer-list.html'
#     context_object_name = 'customer'


# #Product views
def create_product(request):
    forms = ProductForm()
    if request.method == 'POST':
        forms = ProductForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('store:product-list')
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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['order'] = Order.objects.all().order_by('-id')
    #     return context


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


def invoice(request):
    return render(request, 'store/invoice.html')


def view_product(request):
    products = Product.objects.all()
    return render(request, 'store/view-products.html', {'products': products})
