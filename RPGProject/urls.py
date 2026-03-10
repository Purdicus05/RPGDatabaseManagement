"""
URL configuration for RPGProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from RPGApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('characters/',views.characters, name="characters"),
    path('npcs/',views.npcs, name="npc"),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('players/', views.players, name="players"),
    path('armour/', views.armour, name="armour"),
    path('weapons/', views.weapons, name="weapons"),
    path('spells/', views.spells, name="spells"),
    path('classes/', views.classes, name="classes"),

    path('player_add/', views.player_add, name="player_add"),
    path('character_add/', views.character_add, name="character_add"),
    path('character/update/<int:id>/', views.character_update, name="Character_update"),
    path('character/delete/<int:id>/', views.character_delete, name="Character_delete"),
    path('player/update/<int:id>/', views.player_update, name="player_update"),
    path('player/delete/<int:id>/', views.player_delete, name="player_delete"),

    path('npc/update/<int:id>/', views.npc_update, name="npc_update"),
    path('npc/delete/<int:id>/',views.npc_delete,name="npc_delete"),

    path('weapon/update/<int:id>/', views.weapon_update, name="weapon_update"),
    path('weapon/delete/<int:id>/',views.weapon_delete,name="weapon_delete"),
    path('weapon_add',views.weapon_add, name="weapon_add"),

    path('armour/update/int<id>/', views.armour_update, name="armour_update"),
    path('armour/delete/<int:id>/',views.armour_delete,name="armour_delete"),
    path('armour_add',views.armour_add, name="armour_add"),

    path('spell/update/int<id>/', views.spell_update, name="spell_update"),
    path('spell/delete/<int:id>/',views.spell_delete,name="spell_delete"),
    path('spell_add',views.spell_add, name="spell_add"),

    path('class/update/str<id>/', views.class_update, name="class_update"),
    path('class/delete/<str:id>/',views.class_delete,name="class_delete"),
    path('class_add',views.class_add, name="class_add"),

    path('race/update/str<id>/', views.race_update, name="race_update"),
    path('race/delete/<str:id>/',views.race_delete,name="race_delete"),
    path('race_add',views.race_add, name="race_add"),
    path('races/',views.races, name="races"),

    path('logout/',views.logout_view, name="logout"),
]
