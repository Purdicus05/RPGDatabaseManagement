from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# from .models import *

# Create your views here.
def home (request):
    return render(request, 'home.html')

def character(request):
    return render(request, 'characters.html')

def npc(request):
    return render(request, 'npc.html')