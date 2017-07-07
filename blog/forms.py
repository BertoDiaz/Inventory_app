from django import forms
from .models import Element, Order, Product


class ElementForm(forms.ModelForm):

    class Meta:
        model = Element
        fields = ('name', 'maker', 'type_item',)


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('name', 'applicant', 'budget', 'type_of_purchase', 'payment_conditions',
                  'supplier', 'number_product',)


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('description', 'quantity', 'unit_price', 'order',)
        widgets = {'order': forms.HiddenInput()}
