from django.contrib import admin
from .models import Inventory, User, Type


admin.site.register(Inventory)
admin.site.register(User)
admin.site.register(Type)
