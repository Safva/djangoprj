from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fun1(request):
    return HttpResponse('heloo')

def fun2(request):
    return render(request,'home.html')

def fun3(request):
    return render(request,'profile.html')