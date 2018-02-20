from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Customer

def customer_list(request):
    customers = Customer.objects.filter()
    return render(request, 'financial/customer_list.html', {'customers': customers})

    def customer_detail(request, pk):
        customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'customer/customer_detail.html', {'customer': customer})
