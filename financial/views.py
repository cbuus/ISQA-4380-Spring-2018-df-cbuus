from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Customer

def home(request):
    return render(request, 'financial/home.html', {})

def customer_list(request):
    customers = Customer.objects.filter()
    return render(request, 'financial/customer_list.html', {'customers': customers})

def customer_details(request):
    customers = Customer.objects.filter()
    return render(request, 'financial/customer_details.html', {'customers': customers})

def stock_list(request):
    stocks = Stock.objects.filter()
    return render(request, 'financial/stock_list.html', {'stocks': stocks})
