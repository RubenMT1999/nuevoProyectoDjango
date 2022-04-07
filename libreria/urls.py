from django.contrib import admin
from django.urls import path

from libreria.views import mostrar_inicio, crear_objeto

urlpatterns = [
    path('',mostrar_inicio),
    #path('questions/',),
    path('crear/',crear_objeto)
]
