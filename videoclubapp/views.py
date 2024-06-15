from django.shortcuts import render
from .models import Persona

# tarea ...
def inicio(request):
    return render(request, "pages/inicio.html")
def contacto(request):
    return render(request, "pages/contacto.html")

def personas(request):
    personas = Persona.objects.all()
    return render(request, "pages/personas.html", {'personas': personas})

def registrar_persona(request):
    return render(request, "pages/registrar-persona.html")