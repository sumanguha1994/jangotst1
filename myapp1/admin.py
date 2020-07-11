from django.contrib import admin
### inport model
from myapp1.models import Product, Seller, MyShop
# Register your models here.

admin.site.register(MyShop)
admin.site.register(Product)
admin.site.register(Seller)
