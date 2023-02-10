from django.shortcuts import render,HttpResponse,redirect
from .models import models
from datetime import datetime
from nepal.models import destination
from django.contrib.messages import constants as messages
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def Other_designs(request):
    return render(request,"Other_designs.html")
def contact(request):
    if request.method=="POST":
        item_obj=contact.objects.get(id=request.POST.get("id"))
        item=destination
        item_obj.name=request.POST.get("name")
        item_obj.email=request.POST.get("email")
        item_obj.phone=request.POST.get("phone")
        item_obj.save()
        messages.success(request, 'Profile details updated.')

    return render(request,"contact.html")
def login(request):
        if request.method == "POST":
            u_name=request.POST.get("name")
            u_password=request.POST.get("password")
            new_user=User.objects.create_user(u_name,u_password)
            new_user.save()
            return redirect ("index.html")
        return render(request,"login.html")