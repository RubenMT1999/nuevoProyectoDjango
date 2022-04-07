from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


def mostrar_inicio(request):

    lista = Question.objects.all()
    return render(request,'inicio.html',{'Cuestiones':lista})


def crear_objeto(request):

    #GET
    if request.method == 'GET':
        return render(request,'formulario.html')

    #POST
    else:
        objeto_nuevo = Question()
        objeto_nuevo.question_text = request.POST.get('id')
        objeto_nuevo.pub_date = request.POST.get('nombre')
        Question.save(objeto_nuevo)
        return render(request,mostrar_inicio)