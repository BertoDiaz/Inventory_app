from django import forms
from .models import Element


class ElementForm(forms.ModelForm):

    class Meta:
        model = Element
        fields = ('name', 'maker', 'type_item',)
