from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home, name='Home'),
    url(r'^customer$', views.customer_list, name='customer_list'),
    url(r'^customer/(?P<pk>\d+)/$', views.customer_details, name='customer_details'),
    url(r'^customer/(?P<pk>\d+)/delete/$', views.customer_delete, name='customer_delete'),

    url(r'^customer/new/$', views.customer_new, name='customer_new'),
    url(r'^customer/stock/new$', views.stock_new, name='stock_new'),

    url(r'^customer/(?P<pk>\d+)/edit/$', views.customer_edit, name='customer_edit'),
]
