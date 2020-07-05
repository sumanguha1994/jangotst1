from django.conf.urls import include, url
from django.urls import path
from myapp1 import views as myapp1_views

urlpatterns = [
    path('hello/', myapp1_views.hello, name="hello-home"),
    path('mousumi/', myapp1_views.mousumi, name="hello-mousumi"),
    path('koyel/', myapp1_views.koyel, name="hello-koyel"),
    path('suman/<int:age>/<str:name>/', myapp1_views.suman, name="hello-suman"),
    path('suman/<int:age>/', myapp1_views.suman, name="hello-suman"),
    path('suman/', myapp1_views.suman, name="hello-suman"),
]