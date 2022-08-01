from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Congragulations you have created a webapplication using django')
    
def fun1(request):
    return HttpResponse('heloo')

def fun2(request):
    return render(request,'home.html')

def fun3(request):
    return render(request,'profile.html')

def fun4(request):
    return render(request,'about_us.html')