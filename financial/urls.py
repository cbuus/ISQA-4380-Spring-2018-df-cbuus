from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home, name='Home'),
    url(r'^customer', views.customer_list, name='customer_list'),
    url(r'^post/(?P<pk>\d+)/$', views.customer_details, name='customer_details'),
    url(r'^customer/edit/$', views.customer_edit, name='customer_edit'),
]
