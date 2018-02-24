from django.db import models
from django.utils import timezone


class Customer(models.Model):
    customer_ID = models.AutoField(primary_key=True)
    customer_Name = models.CharField(max_length=200)
    customer_StreetAddress =models.CharField(max_length=200)
    customer_City = models.CharField(max_length=200)
    customer_State = models.CharField(max_length=200)
    customer_ZIP = models.CharField(max_length=200)
    customer_Email = models.CharField(max_length=200)
    customer_Phone = models.CharField(max_length=200)
    customer_Created_Date = models.DateTimeField(
                default=timezone.now)
    customer_Modified_Date = models.DateTimeField(
                blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.customer_Name

class Stock(models.Model):
    stock_ID = models.AutoField(primary_key=True)
    stock_Customer = models.ForeignKey('Customer',on_delete=models.CASCADE)
    stock_Symbol = models.CharField(max_length=200)
    stock_Name = models.CharField(max_length=200)
    stock_Number_of_Shares = models.CharField(max_length=200)
    stock_Purchase_Price = models.CharField(max_length=200)
    stock_Purchase_Date = models.CharField(max_length=200)
    stock_Created_Date = models.DateTimeField(
                default=timezone.now)
    stock_Modified_Date = models.DateTimeField(
                blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.stock_Name

class CryptoCurrency(models.Model):
    CryptoCurrency_ID = models.AutoField(primary_key=True)
    CryptoCurrency_Customer = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    CryptoCurrency_Name = models.CharField(max_length=200)
    CryptoCurrency_Number_of_Tokens = models.CharField(max_length=200)
    CryptoCurrency_Purchase_Price = models.CharField(max_length=200)
    CryptoCurrency_Purchase_Date = models.CharField(max_length=200)
    CryptoCurrency_Created_Date = models.DateTimeField(
                default=timezone.now)
    CryptoCurrency_Modified_Date = models.DateTimeField(
                blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.CryptoCurrency_ID
