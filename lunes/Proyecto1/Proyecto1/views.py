from django.shortcuts import render
from django.http import HttpResponse

def saludo(request): #primera vista

  return HttpResponse("Hola alumnos esta es nuestra primera pagina con django")

def despedida(request):

  return HttpResponse("Nos despedimos compañeros")