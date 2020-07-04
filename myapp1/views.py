from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return render(request, 'hello.html', {})
def mousumi(request):
    return render(request, 'mousumi.html', {})
def koyel(request):
    return render(request, 'koyel.html', {})
def suman(request, age = None):
    if(age == None):
        text = "<h1>Only Suman</h1>"
    else:
        text = "<h1>Suman age %s</h1>"%age
    return HttpResponse(text)
# def suman(request, age = None, name = 'KOyel'):
#     if (age == None & name == None): #if (age == None)
#         text = "<h1>Welcome only suman</h1>"
#     elif (age != None | name == None):
#         text = "<h1>Welcome suman %s</h1>"%age
#     elif (age == None | name != None):
#         text = "<h1>Welcome suman with %s</h1>"%name
#     else:
#         text = "<h1>Welcome suman %s with %s</h1>"%age %name
#     return HttpResponse(text)