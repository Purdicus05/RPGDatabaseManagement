from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import *

# Create your views here.
def home (request):
    return render(request, 'home.html')

def character(request):
    return render(request, 'characters.html')

def npc(request):
    return render(request, 'npc.html')

def gm_login (request):
    return render(request, 'gm_login.html')

def player_login (request):
    return render(request, 'player_login.html')

def player_view(request):
    return render(request, 'player_view.html')

def gm_view (request):
    return render(request, 'gm_view.html')

def player_add(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("students")
    else:
        form = PlayerForm()
    return render(request, "player_add.html", {"form": form})