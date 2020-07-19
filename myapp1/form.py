#-*- coding: utf-8 -*-
##################   django form class   ##################
from django import forms
##################   django form class   ##################
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

################################  fields for ModelForm  #########################
# fiels = "__all__"  [all fields which are mentioned in model]
#                        or
# fields = ['fname','lname','email'] [specific fields]
################################  fields for ModelForm  #########################

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

###########################  type of form  ##########################################
# there is 2 type of forms 1.ModelForm 2.Form  
# [but in both case have to use form class]
# forms.ModelForm  => fields = '__all__'  [it requires the Model]
#                       but
# forms.Form       => have to write all the fileds [it does not require the Model]
###########################  type of form  ##########################################

#############################  field  #############################################################
# Commonly used fields and their details 
#
# Name	        Class	                        HTML Input	            Empty value
# BooleanField	class BooleanField(**kwargs)	CheckboxInput	        False
# CharField	    class CharField(**kwargs)	    TextInput	            Whatever you've given as empty_value.
# ChoiceField	class ChoiceField(**kwargs)	    Select	                '' (an empty string)
# DateField	    class DateField(**kwargs)	    DateInput	            None
# DateTimeField	class DateTimeField(**kwargs)	DateTimeInput	        None
# DecimalField	class DecimalField(**kwargs)	NumberInput	            None
# EmailField	class EmailField(**kwargs)	    EmailInput	            '' (an empty string)
# FileField	    class FileField(**kwargs)	    ClearableFileInput	    None
# ImageField	class ImageField(**kwargs)	    ClearableFileInput	    None
#############################  field  #############################################################
