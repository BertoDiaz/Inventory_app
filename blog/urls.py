from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.element_list, name='element_list'),
    url(r'^element/(?P<pk>[0-9]+)/$', views.element_detail, name='element_detail'),
    url(r'^element/new/$', views.element_new, name='element_new'),
    url(r'^element/(?P<pk>[0-9]+)/edit/$', views.element_edit, name='element_edit'),
    url(r'^element/(?P<pk>\d+)/remove/$', views.element_remove, name='element_remove'),
]
