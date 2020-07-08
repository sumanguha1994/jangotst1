from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.http import HttpResponse, HttpResponseNotFound  
from django.views.decorators.http import require_http_methods 
from django.template import loader
from django import template
from datetime import date
import datetime
# get models here
from myapp1.models import Product, Seller, MyShop
# request supported method
@require_http_methods(["GET", "POST", "PUT", "DELETE"])
# Create your views here.
def hello(request):
    today_time = datetime.datetime.now()
    #### check email-id exists or not 
    checking = MyShop.objects.filter(shop_email__exact = "koyel@patlahagu.com").count()
    if(checking <= 0):
        ####  create an entry
        shop = MyShop(
            shop_name = "Bakar Dokan",
            shop_email = "koyel@patlahagu.com",
            shop_location = "Uttar Bamda, Jhargram, 721507",
            shop_phono = "8918569109",
            shop_ownner = "Baka kaka",
        )
        shop.save()
    ####  read all enrtries
    obj = {"shopdetails": MyShop.objects.all().order_by('-id'), "datetime": today_time}
    template = loader.get_template('hello.html')
    return HttpResponse(template.render(obj))
    # return render(request, 'hello.html', {"day_time": today_time, "shopdetails": MyShop.objects.all().order_by('-id')})
def hello_delete(request, id):
    #### get this item by id
    row = get_object_or_404(MyShop, id = id)
    #### delete row
    row.delete()
    return HttpResponseRedirect("/myapp1/hello")




    # def mousumi(request):
    #     today = datetime.datetime.now().date()
    #     daysOfWeek = ['MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN']
    #     obj = {"today": today, "days_of_week": daysOfWeek}
    #     return render(request, 'mousumi.html', obj)
    # def koyel(request):
    #     daysOfWeek = ['MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN']
    #     return render(request, 'koyel.html', {"daysOfWeek": daysOfWeek})
    # def suman(request, age = None, name = None):
    #     if(age == None and name == None):
    #         text = "<h1>name age nai.!!</h1>"
    #     elif (age != None and name == None):
    #         text ="<h1>Age ache %s but name nai</h1>"%age
    #     elif (age == None and name != None):
    #         text ="<h1>Age nai but name ache %s</h1>"%name
    #     else:
    #         text = "<h1>age %s and name %s</h1>"%(age, name)
    #     return HttpResponse(text)