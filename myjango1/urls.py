from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

#################   get static - media url here  ###########################
from myjango1.settings import DEBUG, MEDIA_URL, MEDIA_ROOT, STATIC_URL, STATIC_ROOT
from django.conf.urls.static import static
# from myapp1 import views as myapp1_views

urlpatterns = [
    path('admin/', admin.site.urls, name="admin-home"),
    path('myapp1/', include('myapp1.myapp1url')),
    # path('hello/', myapp1_views.hello, name="hello-home"),
    # path('mousumi/', myapp1_views.mousumi, name="hello-mousumi"),
    # path('koyel/', myapp1_views.koyel, name="hello-koyel"),
    # path('suman/', myapp1_views.suman, name="hello-suman"),
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)