from store import views

from django.urls import path

from .views import (
    create_product,
    create_delivery,
    ProductListView,
    OrderListView,
    DeliveryListView,
    invoice,
    view_product,
)

app_name = "store"

urlpatterns = [
    path('SM-dashboard', views.SM_dashboard, name='SM-dashboard'),

    # path('create-buyer/', create_buyer, name='create-buyer'),
    # path('create-drop/', create_drop, name='create-drop'),
    path('add-product/', create_product, name='add-product'),
    path('invoice/', invoice, name='invoice'),
    path('create-delivery/', create_delivery, name='create-delivery'),

    # path('customer-list/', CustomerListView.as_view(), name='customer-list'),
    path('product-list/', ProductListView.as_view(), name='product-list'),
    path('order-list/', OrderListView.as_view(), name='order-list'),
    path('delivery-list/', DeliveryListView.as_view(), name='delivery-list'),
    path('view-products/', view_product, name='view-product'),
    # path('cart-list/', cart_list, name="cart-list"),
    # path('add-to-cart/<str:slug>/', add_to_cart, name="add-to-cart"),

]
