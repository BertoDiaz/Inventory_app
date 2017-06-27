from django.shortcuts import render
from django.utils import timezone
from .models import Inventory


def inventory_list(request):
    inventories = Inventory.objects.filter(created_date_lte=timezone.now()).order_by('created_date')

    return render(request, 'howdy/inventory_list.html', {'inventories': inventories})
