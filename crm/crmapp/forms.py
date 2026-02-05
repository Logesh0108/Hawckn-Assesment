from django import forms
from .models import Organization, Contact, Product, Order, OrderItem

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'address', 'gst_no']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'organization']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sku', 'base_price', 'offer_percent']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_no', 'contact']


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'size_name', 'qty', 'unit_price', 'customization']
