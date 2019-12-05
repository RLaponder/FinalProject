from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from users.models import *
from django.urls import reverse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login_view(request):
    if request.user.is_authenticated:
        context = {
            "loggedin": True
        }
        return HttpResponse("Hello, you are already logged in.")
    
    if request.method == "POST": 
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("Hello, world. You're at the polls index.")
        else:
            return render(request, "users/login.html", {"message": "Invalid credentials."})

    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {"message": "Logged out."})
