from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^element/$', views.element_list, name='element_list'),
    url(r'^element/(?P<pk>[0-9]+)/$', views.element_detail, name='element_detail'),
    url(r'^element/new/$', views.element_new, name='element_new'),
    url(r'^element/(?P<pk>[0-9]+)/edit/$', views.element_edit, name='element_edit'),
    url(r'^element/(?P<pk>\d+)/remove/$', views.element_remove, name='element_remove'),
    url(r'^order/$', views.order_list, name='order_list'),
    url(r'^order/detail/(?P<pk>[0-9]+)/$', views.order_detail, name='order_detail'),
    url(r'^order/new/$', views.order_new, name='order_new'),
    url(r'^order/new/(?P<pk>[0-9]+)/$', views.order_new_next, name='order_new_next'),
    url(r'^order/(?P<pk>[0-9]+)/edit/$', views.order_edit, name='order_edit'),
    url(r'^order/(?P<pk>\d+)/remove/$', views.order_remove, name='order_remove'),
]
