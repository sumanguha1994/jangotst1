from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import datetime
# Create your views here.
def hello(request):
    today_time = datetime.datetime.now()
    today = date.today()
    totime = datetime.datetime.now().time()
    return render(request, 'hello.html', {"day_time": today_time, "day": today, "time": totime, "bonu": "KOYEL GUHA neogi"})
def mousumi(request):
    return render(request, 'mousumi.html', {})
def koyel(request):
    return render(request, 'koyel.html', {})
def suman(request, age = None, name = None):
    if(age == None and name == None):
        text = "<h1>name age nai.!!</h1>"
    elif (age != None and name == None):
        text ="<h1>Age ache %s but name nai</h1>"%age
    elif (age == None and name != None):
        text ="<h1>Age nai but name ache %s</h1>"%name
    else:
        text = "<h1>age %s and name %s</h1>"%(age, name)
    return HttpResponse(text)