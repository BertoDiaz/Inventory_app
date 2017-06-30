from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from django.utils import timezone
from .models import Element, Order, Product
from .forms import ElementForm, OrderForm, ProductForm


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


def order_list(request):

    orders = Order.objects.filter(created_date__lte=timezone.now()).order_by
    ('created_date')

    return render(request, 'blog/order_list.html', {'orders': orders})


def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    products = Product.objects.filter(order=order.pk).order_by
    ('created_date')

    return render(request, 'blog/order_detail.html', {'order': order, 'products': products})


@login_required
def order_new(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.author = request.user
            order.save()
            # return render(request, 'blog/order_new_next.html', {'order': order,
            #                                                     'num': range(order.number_product)})
            return redirect('blog:order_new_next', pk=order.pk)
    else:
        form = OrderForm()
    return render(request, 'blog/order_new.html', {'form': form})


@login_required
def order_new_next(request, pk):
    order = get_object_or_404(Order, pk=pk)
    ProductFormSet = formset_factory(ProductForm, extra=order.number_product)
    if request.method == "POST":
        # form = ProductForm(request.POST)
        form = ProductFormSet(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            product = form.save(commit=False)
            order = get_object_or_404(Order, pk=pk)
            order.product = product.pk
            order.save()
            product.save()
            print(product)
            return redirect('blog:order_detail', pk=order.pk)
    else:
        # form = ProductForm()
        # order = get_object_or_404(Order, pk=pk)
        formset = ProductFormSet()
    return render(request, 'blog/order_new_next.html', {'formset': formset})


@login_required
def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderForm(data=request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.author = request.user
            order.save()
            return redirect('blog:order_detail', pk=order.pk)
    else:
        form = OrderForm(instance=order)
    return render(request, 'blog/order_edit.html', {'form': form})


@login_required
def order_remove(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('blog:order_list')
