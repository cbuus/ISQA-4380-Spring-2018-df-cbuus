from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Stock
from .forms import CustomerForm

def home(request):
    return render(request, 'financial/home.html', {})

def customer_list(request):
    customers = Customer.objects.all
    return render(request, 'financial/customer_list.html', {'customers': customers})

def customer_details(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'financial/customer_details.html', {'customer': customer})

def stock_details(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    return render(request, 'financial/stock_details.html', {'stock': stock})

def customer_new(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)

        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            return redirect('customer_details', pk=customer.pk)
    else:
        customer = CustomerForm()
    return render(request, 'financial/customer_new.html', {'customer': customer})

def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect('customer_list')

def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        customer = CustomerForm(request.POST, instance=customer)
        if customer.is_valid():
            customer = customer.save(commit=False)
            customer.save()
            return redirect('customer_details', pk=customer.pk)
    else:
        customer = CustomerForm(instance=customer)
    return render(request, 'financial/customer_edit.html', {'customer': customer})

def stock_new(request):
    if request.method == "POST":
        form = StockForm(request.POST)

        if form.is_valid():
            stock = form.save(commit=False)
            stock.save()
            return redirect('customer_details', pk=customer.pk)
    else:
        stock = StockForm()
    return render(request, 'financial/stock_new.html', {'stock': stock})
