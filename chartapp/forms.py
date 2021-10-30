from django import forms
from django.forms import widgets

from . models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields= '__all__'
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'numOfProducts': forms.TextInput(attrs={'class': 'form-control'}),
        }