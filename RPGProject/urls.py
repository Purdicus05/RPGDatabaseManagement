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
from django.urls import path

from RPGApp import views
from RPGApp.views import player_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('characters/',views.character, name="characters"),
    path('npc/',views.npc, name="npc"),
    path('gm_login/', views.gm_login, name="gm_login"),
    path('player_login/', player_login, name="player_login"),
    path('player_view/', views.player_view, name="player_view"),
    path('gm_view/', views.gm_view, name="gm_view"),
    path('player_add/', views.player_add, name="player_add"),
]
