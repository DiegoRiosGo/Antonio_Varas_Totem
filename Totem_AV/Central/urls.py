from django.contrib import admin
from django.urls import path, include
from .views import Principal,Totem

urlpatterns = [
    #html cliente
    path('',Principal,name="Principal"),
    path('Totem/',Totem,name="Totem"),

]