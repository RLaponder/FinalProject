from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from users.models import *
from django.urls import reverse
from socialieven.views import *


def login_view(request):
    if request.user.is_authenticated:
        context = {
            "loggedin": True,
            "message": "Het lijkt erop dat je al ingelogd bent."
        }
        return render(request, "users/error.html", context)
    
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
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return redirect(index)

def register(request):
    return render(request, "users/register.html")

def profiel(request):
    return render(request, "users/profiel.html")
