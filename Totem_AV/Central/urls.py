from django.contrib import admin
from django.urls import path, include
from .views import Principal

urlpatterns = [
    #html cliente
    path('',Principal,name="Principal"),


]