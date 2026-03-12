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



    path('races/',views.races, name="races"),

    path('logout/',views.logout_view, name="logout"),
]
