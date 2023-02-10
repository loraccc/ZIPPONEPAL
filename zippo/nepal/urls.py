from django.urls import path,include
from . import views
from django.contrib import admin
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('Other_designs',views.Other_designs,name='Other_deigns'),
    path('contact',views.contact,name='contact'),

    #user   
    path('login',views.login,name='login'), 
]
