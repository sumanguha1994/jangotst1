from django.conf.urls import include, url
from django.urls import path
from myapp1 import views as myapp1_views

# app_name = 'shop'

urlpatterns = [
    path('hello/', myapp1_views.hello, name="hello-home"),
    path('hello/<int:id>/edit', myapp1_views.hello_single, name="single-shop"),
    path('hello/<int:id>/delete', myapp1_views.hello_delete, name="shop-delete"),
    path('hello/<int:id>/update', myapp1_views.hello_update, name="shop-update"),
    path('hello-product/<int:id>/delete', myapp1_views.hello_product_delete, name="product-delete"),

    # path('mousumi/', myapp1_views.mousumi, name="hello-mousumi"),
    # path('koyel/', myapp1_views.koyel, name="hello-koyel"),
    # path('suman/<int:age>/<str:name>/', myapp1_views.suman, name="hello-suman"),
    # path('suman/<int:age>/', myapp1_views.suman, name="hello-suman"),
    # path('suman/', myapp1_views.suman, name="hello-suman"),
]