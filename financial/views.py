from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Customer
from .forms import CustomerForm

def home(request):
    return render(request, 'financial/home.html', {})

def customer_list(request):
    customers = Customer.objects.all
    return render(request, 'financial/customer_list.html', {'customers': customers})

def customer_details(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'financial/customer_details.html', {'customer': customer})

def customer_edit(request):
    customer = CustomerForm()
    return render(request, 'financial/customer_edit.html', {'customer': customer})
