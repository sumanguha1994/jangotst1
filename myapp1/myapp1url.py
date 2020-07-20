from django.conf.urls import include, url
from django.urls import path
from myapp1 import views as myapp1_views
######################  generic view start ##########################
####  static/template view  ####
from myapp1.views import StaticView
####  listview    ####
from django.views.generic import ListView
######################  generic view end   ##########################
from myapp1.models import Product
# app_name = 'shop'

urlpatterns = [
    #########################   classic view   ##############################
    path('hello/', myapp1_views.hello, name="hello-home"),
    path('hello/<int:id>/edit', myapp1_views.hello_single, name="single-shop"),
    path('hello/<int:id>/delete', myapp1_views.hello_delete, name="shop-delete"),
    path('hello/<int:id>/update', myapp1_views.hello_update, name="shop-update"),
    path('hello-product/<int:id>/delete', myapp1_views.hello_product_delete, name="product-delete"),
    path('hello-seller/<int:id>/delete', myapp1_views.hello_seller_delete, name="seller-delete"),
    path('product-entry/', myapp1_views.product_entry, name="product-entry-form"),
    path('seller-entry/', myapp1_views.seller_entry, name="seller-entry-form"),
    path('set-get-file/<str:name>/', myapp1_views.set_name_get_file, name="set-name-get-file"),
    #########################   generic view   ##############################
    path('koyel-static/', StaticView.as_view()),                                         ########=======generic static/template view========#######
    path('product-static-list/', ListView.as_view(                                       ########=======generic list view========#######
            model = Product, template_name = "mousumi.html", context_object_name = "products_list")), 
]

# path('mousumi/', myapp1_views.mousumi, name="hello-mousumi"),
# path('koyel/', myapp1_views.koyel, name="hello-koyel"),
# path('suman/<int:age>/<str:name>/', myapp1_views.suman, name="hello-suman"),
# path('suman/<int:age>/', myapp1_views.suman, name="hello-suman"),
# path('suman/', myapp1_views.suman, name="hello-suman"),