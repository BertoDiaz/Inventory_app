from djnago.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.inventory_list),
]
