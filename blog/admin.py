from django.contrib import admin
from .models import Element, Type, Order, Budget, Type_of_purchase, Payment, Supplier, Product

admin.site.register(Element)
admin.site.register(Type)
admin.site.register(Order)
admin.site.register(Budget)
admin.site.register(Type_of_purchase)
admin.site.register(Payment)
admin.site.register(Supplier)
admin.site.register(Product)
