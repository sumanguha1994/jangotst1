from django.shortcuts import get_object_or_404, render, HttpResponseRedirect, redirect
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
######################  model form  #################################
from myapp1.form import ProductForm, SellerForm
######################  model form  #################################
######################  file uploading function import ##############
from myapp1.funtions import handle_uploaded_file 
######################  file uploading function import ##############
###################### use middleware in template ###################
from django.template.response import TemplateResponse
###################### use middleware in template ###################
from django.template import loader
from django import template
from datetime import date
import datetime
###################### csv | pdf ####################################
import csv
from reportlab.pdfgen import canvas
###################### csv | pdf ####################################
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
    shopPaginator = Paginator(shopobj, 5)
    page_number = request.GET.get('page')
    shop_page_obj = shopPaginator.get_page(page_number)

    productobj = Product.objects.all().order_by('created_at')
    proPaginator = Paginator(productobj, 8)
    page_number = request.GET.get('page')
    pro_page_obj = proPaginator.get_page(page_number)

    sellerobj = Seller.objects.all()
    sellerPaginator = Paginator(sellerobj, 5)
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
######################  modelform     ##########################
@csrf_exempt
def product_entry(request):
    if (request.method == 'GET'):
        #######################    using session   #############################
        # del request.session['test']
        # if 'test' not in request.session:
        if not request.session.has_key('test'):
            request.session['test'] = "test1 1st time session initialized.."
            request.session['test1'] = "WOW!! session is on!!!"
        else:
            del request.session['test']
            request.session['test'] = "test2 2nd time session initialized."
            request.session['test1'] = "WOW!! session changed!!!"
        #######################    using session   #############################
        proForm = ProductForm()
        sesobj = {"ses1": request.session.get('test'), "ses2": request.session.get('test1')}
        obj = {"proform": proForm.as_ul(), "form":"product", "ses": sesobj}   ######   as_ul() [list wise form shows in html page]
        template = loader.get_template("modelform.html")
        return HttpResponse(template.render(obj))
    else:
        ProductFormValue = ProductForm(request.POST)
        if ProductFormValue.is_valid():
            ProductFormValue.save()
            return HttpResponseRedirect("/myapp1/product-static-list")
        else:
            proForm = ProductForm()
            obj = {"proform": proForm.as_p(), "form":"product"}  
            template = loader.get_template("modelform.html")
            return HttpResponse(template.render(obj))
@csrf_exempt
def seller_entry(request):
    if(request.method == 'GET'):
        response = HttpResponse()
        ####################  using cookie  #####################
        response.set_cookie("name", "suman")
        ## set cookies    => response.set_cookie("key", "value")
        ## get cookies    => response.COOKIES.get("key") | request.COOKIES['key']
        ## delete cookies => response.delete_cookie("key")
        cookieobj = {"cook": request.COOKIES.get("key")}
        ####################  using cookie  #####################
        selForm = SellerForm()
        obj = {"selform": selForm.as_p(), "form": "seller", "cook": cookieobj}    #######  as_p() [paragraph wise form shows in html page]
        template = loader.get_template("modelform.html")
        response = HttpResponse(template.render(obj))
        return response
    else:
        SellerFormValue = SellerForm(request.POST, request.FILES)
        if SellerFormValue.is_valid():
            ##################  file uploading function   ##############
            handle_uploaded_file(request.FILES['seller_pic'], 'seller')
            SellerFormValue.save()
            return HttpResponseRedirect("/myapp1/hello")
        else:
            return HttpResponseRedirect("/myapp1/seller-entry")
######################  modelform     ##########################
######################  csv | pdf     ##########################
def set_name_get_file(request, name = None):
    if name == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="file.csv"'
        product = Product.objects.all()
        writer = csv.writer(response)
        for pro in product:
            writer.writerow([pro.id, pro.product_name, pro.price, pro.mfd, pro.updated_at])
        return response
    else:
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="file.pdf"'
        p = canvas.Canvas(response)
        p.setFont("Times-Roman", 55)
        # product = Product.objects.all()
        p.drawString(100,700, "Hello, Javatpoint.")
        p.showPage()
        p.save()
        return response
######################  csv | pdf     ##########################

        
        























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
#  ex::::: return redirect(product_entry)
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

################### model form show ####################################################
#   as_ul()    [add like this in view.py page] [list wise form shows in html page]
#   as_p()     [add like this in view.py page] [paragraph wise form shows in html page]
#   as_table() [add like this in view.py page] [table wise form shows up in html page]
#                         OR
#   {{objname.as_ul}}    [add like this in html view page]
#   {{objname.as_p}}     [add like this in html view page]
#   {{objname.as_table}} [add like this in html view page]
################### model form show ####################################################

################### moddleware ###############################################
# middleware does work without using of -> "TemplateResponse"
################### moddleware ###############################################
