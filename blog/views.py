from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Element
from .forms import ElementForm


def element_list(request):

    elements = Element.objects.filter(created_date__lte=timezone.now()).order_by
    ('created_date')

    return render(request, 'blog/element_list.html', {'elements': elements})


def element_detail(request, pk):
    element = get_object_or_404(Element, pk=pk)

    return render(request, 'blog/element_detail.html', {'element': element})


@login_required
def element_new(request):
    if request.method == "POST":
        form = ElementForm(request.POST)
        if form.is_valid():
            element = form.save(commit=False)
            element.author = request.user
            # element.published_date = timezone.now()
            element.save()
            return redirect('blog:element_detail', pk=element.pk)
    else:
        form = ElementForm()
    return render(request, 'blog/element_edit.html', {'form': form})


@login_required
def element_edit(request, pk):
    element = get_object_or_404(Element, pk=pk)
    if request.method == "POST":
        form = ElementForm(data=request.POST, instance=element)
        if form.is_valid():
            element = form.save(commit=False)
            element.author = request.user
            element.save()
            return redirect('blog:element_detail', pk=element.pk)
    else:
        form = ElementForm(instance=element)
    return render(request, 'blog/element_edit.html', {'form': form})


@login_required
def element_remove(request, pk):
    element = get_object_or_404(Element, pk=pk)
    element.delete()
    return redirect('blog:element_list')
