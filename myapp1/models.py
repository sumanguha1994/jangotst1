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
    phone_no = models.IntegerField(max_length=100, blank=True, null=True)
    email_id = models.EmailField(max_length=255, blank=True, null=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class MyShop(models.Model):
    shop_name = models.CharField(max_length=100)
    shop_email = models.EmailField(max_length=100)
    shop_location = models.TextField()
    shop_phono = models.IntegerField(null=False, blank=False)
    shop_ownner = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "ShopDetail"

