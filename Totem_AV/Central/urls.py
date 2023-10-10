from django.contrib import admin
from django.urls import path, include
from .views import Principal,formulario

urlpatterns = [
    #html cliente
    path('',Principal,name="Principal"),
    path('formulario/',formulario,name="formulario"),

]