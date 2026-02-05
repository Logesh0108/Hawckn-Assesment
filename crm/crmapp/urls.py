from django.urls import path
from . import views
from .views import (
    add_organization, add_contact,
    add_product, add_order, add_order_item
)

urlpatterns = [
    path('', views.home, name='home'),
    path('organizations/', views.organizations, name='organizations'),
    path('contacts/', views.contacts, name='contacts'),
    path('products/', views.products, name='products'),
    path('orders/', views.orders, name='orders'),
    path('add/organization/', add_organization, name='add_organization'),
    path('add/contact/', add_contact, name='add_contact'),
    path('add/product/', add_product, name='add_product'),
    path('add/order/', add_order, name='add_order'),
    path('add/order-item/', add_order_item, name='add_order_item'),

]
from .api_views import *

urlpatterns += [
    path('api/organizations/', organizations_api),
    path('api/contacts/', contacts_api),
    path('api/products/', products_api),
    path('api/orders/', orders_api),
    path('api/order-items/', order_items_api),
]
