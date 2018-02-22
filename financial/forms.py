from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('customer_Name', 'customer_StreetAddress','customer_City','customer_State','customer_ZIP','customer_Email','customer_Phone',
        )
