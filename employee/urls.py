from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.fun1),
    path('myhome',views.fun2),
    path('myprofile',views.fun3),
    path('aboutus',views.fun4)
]

