from django.urls import path
from . import views


urlpatterns = [
    path('home',views.fun1),
    path('myhome',views.fun2),
    path('myprofile',views.fun3)
]

