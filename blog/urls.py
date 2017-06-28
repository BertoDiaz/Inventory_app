from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.element_list),
    url(r'^element/(?P<pk>[0-9]+)/$', views.element_detail),
    url(r'^element/new/$', views.element_new, name='element_new'),
    url(r'^element/(?P<pk>[0-9]+)/edit/$', views.element_edit, name='element_edit'),
]
