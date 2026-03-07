from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')


def home (request):
    return render(request, 'home.html')

def characters(request):
    return render(request, 'characters.html')

def npcs(request):
    return render(request, 'npc.html')

def players(request):
    return render(request, 'players.html')

def weapons(request):
    return render(request, 'weapons.html')

def armour(request):
    return render(request, 'armour.html')

def spells(request):
    return render(request, 'spells.html')

def races(request):
    return render(request, 'races.html')

def classes(request):
    return render(request, 'classes.html')



def login (request):
    return render(request, 'login.html')

def player_add(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PlayerForm()
    return render(request, "player_add.html", {"form": form})