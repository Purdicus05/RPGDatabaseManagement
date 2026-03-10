from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def home (request):
    return render(request, 'home.html')
@login_required(login_url='/')
def characters(request):
    character_list = Characters.objects.select_related("character_playerid").all().order_by("character_name")
    return render(request, 'characters.html', {'Characters': character_list})
@login_required(login_url='/')
def npcs(request):
    npc_list = Npc.objects.select_related('npc_weaponid').select_related('npc_spellid').all().order_by("npc_type")
    return render(request, 'npc.html', {'npcs': npc_list})
@login_required(login_url='/')
def players(request):
    player_list = Players.objects.all().order_by("player_surname")
    return render(request, 'players.html', {'Players': player_list})
@login_required(login_url='/')
def weapons(request):
    weapon_list = Weapons.objects.all().order_by("weapon_name")
    return render(request, 'weapons.html', {'Weapons': weapon_list})
@login_required(login_url='/')
def armour(request):
    armour_list = Armour.objects.all().order_by("armour_name")
    return render(request, 'armour.html', {'Armour': armour_list})
@login_required(login_url='/')
def spells(request):
    spell_list = Spells.objects.all().order_by("spell_name")
    return render(request, 'spells.html', {'Spells': spell_list})
@login_required(login_url='/')
def races(request):
    race_list = Races.objects.all().order_by("race_name")
    return render(request, 'races.html', {'Races': race_list})
@login_required(login_url='/')
def classes(request):
    class_list = Classes.objects.all().order_by("class_name")
    return render(request, 'classes.html', {'Classes': class_list})
@login_required(login_url='/')

def login (request):
    return render(request, 'login.html')
@login_required(login_url='/')
def player_add(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("players")
    else:
        form = PlayerForm()
    return render(request, "player_add.html", {"form": form})
@login_required(login_url='/')
def player_update(request):
    return render(request, 'player_update.html')
@login_required(login_url='/')
def player_delete(request):
    return render(request, 'player_delete.html')
@login_required(login_url='/')
def character_add(request):

    return render(request, 'character_add.html')
@login_required(login_url='/')
def character_delete(request):
    return render(request, 'character_delete.html')
@login_required(login_url='/')
def character_update(request):
    return render(request, 'character_update.html')
@login_required(login_url='/')
def npc_delete(request):
    return render(request, 'npc_delete.html')
@login_required(login_url='/')
def npc_update(request):
    return render(request, 'npc_update.html')
@login_required(login_url='/')
def weapon_delete(request):
    return render(request, 'weapon_delete.html')
@login_required(login_url='/')
def weapon_update(request):
    return render(request, 'weapon_update.html')
@login_required(login_url='/')
def weapon_add(request):
    return render(request, 'weapon_add.html')
@login_required(login_url='/')
def armour_delete(request):
    return render(request, 'armour_delete.html')
@login_required(login_url='/')
def armour_update(request):
    return render(request, 'armour_update.html')
@login_required(login_url='/')
def armour_add(request):
    return render(request, 'armour_add.html')
@login_required(login_url='/')
def spell_delete(request):
    return render(request, 'spell_delete.html')
@login_required(login_url='/')
def spell_update(request):
    return render(request, 'spell_update.html')
@login_required(login_url='/')
def spell_add(request):
    return render(request, 'spell_add.html')
@login_required(login_url='/')
def class_delete(request):
    return render(request, 'class_delete.html')
@login_required(login_url='/')
def class_update(request):
    return render(request, 'class_update.html')
@login_required(login_url='/')
def class_add(request):
    return render(request, 'class_add.html')
@login_required(login_url='/')
def race_delete(request):
    return render(request, 'race_delete.html')
@login_required(login_url='/')
def race_update(request):
    return render(request, 'race_update.html')
@login_required(login_url='/')
def race_add(request):
    return render(request, 'race_add.html')