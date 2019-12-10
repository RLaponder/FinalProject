from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from users.models import *
from django.urls import reverse
from socialieven.views import *
import datetime

# Use custom User model.
from django.contrib.auth import get_user_model
User = get_user_model()


def logout_view(request):
    # Log user out and go to index.
    logout(request)
    return redirect(index)

def register(request):
    # If a user submits the register form, do the following.
    if request.method == "POST": 
        # Get all the information from the register for and create user.
        user = User.objects.create_user(username=request.POST["gebruikersnaam"], email=request.POST["email1"], password=request.POST["wachtwoord1"])
        user.first_name = request.POST["voornaam"]
        user.last_name = request.POST["achternaam"]
        user.geboortedatum = request.POST["geboortedatum"]
        user.straat = request.POST["straat"]
        user.huisnummer = int(request.POST["huisnummer"])
        user.postcode = request.POST["postcode"]
        user.woonplaats = request.POST["woonplaats"]
        user.gebouw = int(request.POST["gebouw"])
        user.verdieping = int(request.POST["verdieping"])
        user.save()
        
        # Succesfull registration, go to index.
        context = {
            "loggedin": False,
            "message": "You have succesfully registered."
        }
        return render(request, "users/index.html", context)
    
    # If a user did not (yet) register, show the register form.
    return render(request, "users/register.html")

def profiel(request):
    # Go to login page if the user has not logged in.
    if not request.user.is_authenticated:
        context = {
            "loggedin": False
        }
        return render(request, "users/index.html", context)
    
    # Show the profile of the current user.
    context = {
        "user": request.user,
        "loggedin": True
    }
    return render(request, "users/profiel.html", context)
