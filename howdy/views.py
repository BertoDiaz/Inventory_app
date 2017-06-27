from django.shortcuts import render


def inventory_list(request):
    return render(request, 'howdy/inventory_list.html', {})
