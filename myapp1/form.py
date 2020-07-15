#-*- coding: utf-8 -*-
from django import forms
from myapp1.models import Product, Seller

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = "__all__"
    # product_name = forms.CharField(max_length=100)
    # price = forms.CharField(max_length=100)
    # mfd = forms.DateTimeField(auto_now_add=False)  
    # password = forms.CharField(widget = forms.PasswordInput())     #### for any password field ####