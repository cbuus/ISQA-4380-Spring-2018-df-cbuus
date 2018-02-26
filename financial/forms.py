from django import forms
from .models import Customer
from .models import Stock

class StockForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = ('stock_Name',
        )

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('customer_Name', 'customer_StreetAddress','customer_City','customer_State','customer_ZIP','customer_Email','customer_Phone',
        )
