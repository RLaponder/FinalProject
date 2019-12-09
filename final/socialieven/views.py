from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from users.models import *
from django.urls import reverse

def index(request):
    if request.method == "POST": 
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return render(request, "users/index.html")
        else:
            context = {
                "loggedin": False,
                "message": "Het ingevoerde e-mail adres of wachtwoord is onjuist."
            }
            return render(request, "users/error.html", context)
    
    # Show index page if a user is logged in.
    if not request.user.is_authenticated:
        context = {
            "loggedin": False
        }
    else:
        context = {
            "user": request.user,
            "loggedin": True
        }
    return render(request, "users/index.html", context)

def activiteiten(request):
    if not request.user.is_authenticated:
        context = {
            "loggedin": False
        }
        return render(request, "users/login.html", context)
    return render(request, "users/activiteiten.html")

def nieuwe_activiteit(request):
    
    return render(request, "users/nieuwe_activiteit.html")
