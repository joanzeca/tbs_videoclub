from django.shortcuts import render
from .models import Persona

# tarea ...
def inicio(request):
    return render(request, "inicio.html")
def programas(request):
    return render(request, "programas.html")
def talleres(request):
    return render(request, "talleres.html")
def asesoramiento(request):
    return render(request, "asesoramiento.html")
def contacto(request):
    return render(request, "contacto.html")

def personas(request):
    personas = Persona.objects.all()
    return render(request, "personas.html", {'personas': personas})