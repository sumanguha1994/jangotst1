from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.http import HttpResponse, HttpResponseNotFound  
from django.views.decorators.http import require_http_methods 
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
######################  sending mail start ##########################
from django.core.mail import send_mail
from django.conf import settings
######################  sending mail end   ##########################  
######################  generic view start ##########################
from django.views.generic import TemplateView
######################  generic view end   ##########################
from django.template import loader
from django import template
from datetime import date
import datetime
# get models here
from myapp1.models import Product, Seller, MyShop
# request supported method
@require_http_methods(["GET", "POST", "PUT", "DELETE"])
# Create your classic views here.
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
    shopobj = MyShop.objects.all().order_by('-id')
    shopPaginator = Paginator(shopobj, 3)
    page_number = request.GET.get('page')
    shop_page_obj = shopPaginator.get_page(page_number)

    productobj = Product.objects.all().order_by('created_at')
    proPaginator = Paginator(productobj, 8)
    page_number = request.GET.get('page')
    pro_page_obj = proPaginator.get_page(page_number)

    sellerobj = Seller.objects.all()
    sellerPaginator = Paginator(sellerobj, 3)
    page_number = request.GET.get('page')
    seller_page_obj = sellerPaginator.get_page(page_number)

    obj = {"shopdetails": shop_page_obj, "products": pro_page_obj, "sellers": seller_page_obj, "datetime": today_time}
    template = loader.get_template('hello.html')
    return HttpResponse(template.render(obj))
    # return render(request, 'hello.html', {"day_time": today_time, "shopdetails": MyShop.objects.all().order_by('-id')})
def hello_delete(request, id):
    #### get this item by id
    row = get_object_or_404(MyShop, id = id)
    #### delete row
    row.delete()
    return HttpResponseRedirect("/myapp1/hello")
def hello_single(request, id):
    today_time = datetime.datetime.now()
    row = get_object_or_404(MyShop, id = id)
    obj = {"edit": 1, "shop": 1, "editval": row, "shopdetails": MyShop.objects.all().order_by('-id'), "datetime": today_time}
    template = loader.get_template('hello.html')
    return HttpResponse(template.render(obj))
@csrf_exempt
def hello_update(request, id):
    # today_time = datetime.datetime.now()
    row = get_object_or_404(MyShop, id = id)
    ### shop name
    if(request.POST['shopname'] != None):
        row.shop_name = request.POST['shopname']
    else:
        row.shop_name = row.shop_name
    ### shop email
    if(request.POST['emailid'] != None):
        row.shop_email = request.POST['emailid']
    else:
        row.shop_email = row.shop_email
    ### shop location
    if(request.POST['location'] != None):
        row.shop_location = request.POST['location']
    else:
        row.shop_location = row.shop_location
    ### shop phoneno
    if(request.POST['phoneno'] != None):
        row.shop_phono = request.POST['phoneno']
    else:
        row.shop_phono = row.shop_phono
    ### shop owner
    if(request.POST['owername'] != None):
        row.shop_ownner = request.POST['owername']
    else:
        row.shop_ownner = row.shop_ownner
    row.save()
    # obj = {"shopdetails": MyShop.objects.all().order_by('-id'), "datetime": today_time}
    # template = loader.get_template('hello.html')
    return HttpResponseRedirect("/myapp1/hello")
    # return HttpResponse(template.render(obj))
def hello_product_delete(request, id):
    row = get_object_or_404(Product, id = id)
    row.delete()
    # return HttpResponse(row)
    return HttpResponseRedirect("/myapp1/hello")
def hello_seller_delete(request, id):
    row = get_object_or_404(Seller, id = id)
    row.delete()
    return HttpResponseRedirect("/myapp1/hello")
######################  generic view  ##########################
class StaticView(TemplateView):
    template_name = "koyel.html"
######################  generic view  ##########################


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


###################  rendaring to another function  ##################################
# def viewArticle(request, articleId):
#    """ A view that display an article based on his ID"""
#    text = "Displaying article Number : %s" %articleId
#    return redirect(viewArticles, year = "2045", month = "02")
	
# def viewArticles(request, year, month):
#    text = "Displaying articles of : %s/%s"%(year, month)
#    return HttpResponse(text)
###################  rendaring to another function  ##################################


###################  sending mail  ##################################
# def email(request):
#     subject = 'Thank you for registering to our site'
#     message = ' it  means a world to us '
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = ['receiver@gmail.com']
#     send_mail( subject, message, email_from, recipient_list )
#     return redirect('redirect to a new page')
###################  sending mail  ##################################

