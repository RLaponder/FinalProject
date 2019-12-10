from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from users.models import *
from django.urls import reverse

def index(request):
    # If user tries to login, do the following.
    if request.method == "POST": 
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            context = {
                "loggedin": True
            }
            return redirect(index)
        else:
            context = {
                "loggedin": False,
                "message": "Het ingevoerde e-mail adres of wachtwoord is onjuist."
            }
            return render(request, "users/error.html", context)
    
    # Check whether a user is logged in, and go to index.
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
    # If current user is not logged in, go to index.
    if not request.user.is_authenticated:
        context = {
            "loggedin": False
        }
        return render(request, "users/index.html", context)
    return render(request, "users/activiteiten.html")

def nieuwe_activiteit(request):
    # If current user is not logged in, go to index.
    if not request.user.is_authenticated:
        context = {
            "loggedin": False
        }
        return render(request, "users/index.html", context)

    # If the user submits the activity form, do the following.
    if request.method == "POST": 
        # Create a new activity for this user.
        activiteit = Activiteit(gebruiker=request.user)
        # Add all the entered information from the form to the created activity.
        activiteit.name = request.POST["naam"]
        activiteit.datum = request.POST["datum"]
        activiteit.starttijd = request.POST["starttijd"]
        activiteit.eindtijd = request.POST["eindtijd"]
        activiteit.straat = request.POST["straat"]
        activiteit.huisnummer = int(request.POST["huisnummer"])
        activiteit.postcode = request.POST["postcode"]
        activiteit.plaats = request.POST["plaats"]
        activiteit.gebouw = int(request.POST["gebouw"])
        activiteit.verdieping = int(request.POST["verdieping"])
        activiteit.categorie = request.POST["categorie"]
        if request.POST["uitgenodigd"] == "Ja":
            activiteit.uitgenodigd = True
        else:
            activiteit.uitgenodigd = False
        activiteit.beschrijving = request.POST["beschrijving"]
        activiteit.save()

        context = {
            "message": "Succes! Je activiteit is toegevoegd.",
            "loggedin": True
        }
        return render(request, "users/nieuwe_activiteit.html", context)
    
    # Show the form.
    context = {
        "loggedin": True
    }
    return render(request, "users/nieuwe_activiteit.html")
