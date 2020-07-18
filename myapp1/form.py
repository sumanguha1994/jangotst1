#-*- coding: utf-8 -*-
from django import forms
from django.forms import ValidationError
from myapp1.models import Product, Seller

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = "__all__"


###########################   custome validation   ##########################
# class ProductForm(forms.Form):
#     product_name = forms.CharField()
#     price = forms.CharField()
#     mfd = forms.DateTimeField()  
    
#     def clean_product_name(self):
#         super().clean()
#         proname = self.cleaned_data.get("product_name")
#         dbpro = Product.objects.filter(product_name = proname).exists()

#         if dbpro:
#             raise forms.ValidationError("Product Already Exists")
#         return proname
    
#     def clean_price(self):
#         super().clean()
#         proprice = self.cleaned_data.get("price")

#         if len(proprice) < 3:
#             raise forms.ValidationError("Price Can't be less than 3 digit.")
#         return proprice
###########################   custome validation   ##########################
