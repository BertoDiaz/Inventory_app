from django.contrib import admin
from .models import Element, Type, Order, Budget, Buy_Type, Payment, Provider, Product

admin.site.register(Element)
admin.site.register(Type)
admin.site.register(Order)
admin.site.register(Budget)
admin.site.register(Buy_Type)
admin.site.register(Payment)
admin.site.register(Provider)
admin.site.register(Product)
