from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    mfd = models.DateTimeField(auto_now_add=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Seller(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    seller_name = models.CharField(max_length=100)
    # phone_no = models.IntegerField(max_length=100, blank=True, null=True)
    phone_no = models.IntegerField(blank=True, null=True)
    email_id = models.EmailField(max_length=255, blank=True, null=True)
    address = models.TextField()
    ## add a new column after everything is set in model
    seller_pic = models.ImageField(upload_to='seller', max_length=100, default='N/A')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class MyShop(models.Model):
    shop_name = models.CharField(max_length=100)
    shop_email = models.EmailField(max_length=100)
    shop_location = models.TextField()
    shop_phono = models.IntegerField(null=False, blank=False)
    shop_ownner = models.CharField(max_length=100, null=False, blank=False)
    ## add a new column after everything is set in model
    shop_owner_pic = models.ImageField(upload_to='shop', max_length=100, default="N/A")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "ShopDetail"

