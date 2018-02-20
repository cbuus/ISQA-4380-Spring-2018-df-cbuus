from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home, name='Home'),
    url(r'^customer', views.customer_list, name='customer_list'),
    url(r'^customer/detail', views.customer_details, name='customer_detail'),

]
