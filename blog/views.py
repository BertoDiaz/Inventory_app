from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
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
        product = ProductForm()
        # print(product)
        formset = ProductFormSet(request.POST)
        # print(form)
        if (formset.is_valid()):
            for form in formset:
                # print(form)
                product = form.cleaned_data
                product = form.save(commit=False)
                # print(product)
                # order = get_object_or_404(Order, pk=pk)
                # product.order = pk
                # order.save()
                # product.save
                # print(order)
                # print(order.pk)
                product.order = order
                # print(product)
                product.save()

            return redirect('blog:order_detail', pk=order.pk)
    else:
        # form = ProductForm()
        # order = get_object_or_404(Order, pk=pk)
        formset = ProductFormSet()
    return render(request, 'blog/order_new_next.html', {'formset': formset})


@login_required
def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)
    products = Product.objects.filter(order=order.pk).order_by('created_date')
    ProductFormSet = formset_factory(ProductForm)
    if request.method == "POST":
        order_form = OrderForm(data=request.POST, instance=order, prefix="orderForm")
        # products = Product.objects.filter(order=order.pk).order_by('created_date')
        # print(products[0])
        formset = ProductFormSet(data=request.POST, prefix="productForm")
        # products_form = ProductForm(data=request.POST, prefix="productForm")
        # print(order_form)
        # print(products_form)
        print(len(products))
        if order_form.is_valid() and formset.is_valid():
            order = order_form.save(commit=False)
            order.author = request.user
            order.save()
            # num = 0
            # for form in formset:
            for num in range(0, len(products)):
                # print(form)
                # products = form.cleaned_data
                product = formset[num].save(commit=False)
                product.order = order
                if products[num].description != product.description:
                    products[num].description = product.description

                if products[num].quantity != product.quantity:
                    products[num].quantity = product.quantity

                if products[num].unit_price != product.unit_price:
                    products[num].unit_price = product.unit_price

                products[num].save()
                # num = num + 1
                # form.save()
            return redirect('blog:order_detail', pk=order.pk)
    else:
        order_form = OrderForm(instance=order, prefix="orderForm")
        products = Product.objects.filter(order=order.pk).order_by('created_date')
        # print(products[0])
        # num = 0
        # products_form = [0, 0]
        # for product in products:
        #     products_form[num] = ProductForm(instance=product, prefix="productForm")
        #     num = num + 1
        products_formset = ProductFormSet(initial=[{'description': form.description,
                                                    'quantity': form.quantity,
                                                    'unit_price': form.unit_price}
                                                   for form in products], prefix="productForm")
    return render(request, 'blog/order_edit.html', {'order_form': order_form,
                                                    'products_formset': products_formset})


@login_required
def order_remove(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('blog:order_list')
