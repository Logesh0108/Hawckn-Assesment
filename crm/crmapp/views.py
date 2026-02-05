from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

from django.shortcuts import render
from .models import Organization, Contact, Product, Order

def organizations(request):
    data = Organization.objects.all()
    return render(request, 'organizations.html', {'data': data})


def contacts(request):
    data = Contact.objects.select_related('organization')
    return render(request, 'contacts.html', {'data': data})


def products(request):
    data = Product.objects.all()
    return render(request, 'products.html', {'data': data})

def orders(request):
    orders = Order.objects.select_related('contact')
    return render(request, 'orders.html', {'orders': orders})


from django.shortcuts import render, redirect
from .forms import (
    OrganizationForm, ContactForm,
    ProductForm, OrderForm, OrderItemForm
)

def add_organization(request):
    form = OrganizationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('organizations')
    return render(request, 'form.html', {'form': form, 'title': 'Add Organization'})


def add_contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('contacts')
    return render(request, 'form.html', {'form': form, 'title': 'Add Contact'})


def add_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('products')
    return render(request, 'form.html', {'form': form, 'title': 'Add Product'})


def add_order(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('orders')
    return render(request, 'form.html', {'form': form, 'title': 'Add Order'})


def add_order_item(request):
    form = OrderItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('orders')
    return render(request, 'form.html', {'form': form, 'title': 'Add Order Item'})
