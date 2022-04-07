from django.contrib import admin
from django.urls import path

from libreria.views import mostrar_inicio

urlpatterns = [
    path('',mostrar_inicio),
    #path('questions/',),
    #path('questions/crear',)
]
